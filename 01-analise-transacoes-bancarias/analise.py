import csv

def ler_transacoes(dados_transacoes):
    transacoes = []

    try:
        with open(dados_transacoes, mode='r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)

            for linha in leitor:
                transacoes.append(linha)

    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as erro:
        print(f"Erro inesperado: {erro}")

    return transacoes

def calcular_resumo(transacoes):
    total_entradas = 0
    total_saidas = 0

    for transacoes in transacoes:
        valor = float(transacoes["TransactionAmount"])
        tipo = transacoes["TransactionType"].lower()

        if tipo == "credit":
            total_entradas += valor
        elif tipo == "debit":
            total_saidas += valor

    saldo_final = total_entradas - total_saidas

    return total_entradas,total_saidas,saldo_final
