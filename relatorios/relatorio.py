import csv

def gerar_relatorio(dados):
    valores = []

    #Lendo o arquivo CSV
    with open(dados, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            try:
                valor = float(linha["TransactionAmount"])
                valores.append(valor)
            except ValueError:
                # ignora linhas inválidas
                continue

    if not valores:
        return None

    total_transacoes = len(valores)
    valor_total = sum(valores)
    maior_operacao = max(valores)
    menor_operacao = min(valores)

    return {
        "total_transacoes": total_transacoes,
        "valor_total": valor_total,
        "maior_operacao": maior_operacao,
        "menor_operacao": menor_operacao,
    }
