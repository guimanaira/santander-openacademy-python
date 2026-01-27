from extracao import extrair_dados
from transformacao import transformar_dados
from carga import carregar_relatorio

def main():
    dados = extrair_dados("dados.csv")
    resultado = transformar_dados(dados)
    carregar_relatorio(resultado)

if __name__ == "__main__":
    main()
    