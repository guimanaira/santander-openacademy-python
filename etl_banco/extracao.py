import csv

def extrair_dados(caminho_arquivo):
    dados = []

    try:
        with open(caminho_arquivo, mode="r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                dados.append(linha)

    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as erro:
        print(f"Erro ao extrair dados: {erro}")

    return dados
