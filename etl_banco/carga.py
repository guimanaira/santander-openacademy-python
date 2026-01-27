def carregar_relatorio(resultado):
    try:
        with open("relatorio_final.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write("RELATORIO BANCÁRIO\n")
            arquivo.write(f"Total de Depósitos: R$ {resultado['total_depositos']:.2f}\n")
            arquivo.write(f"Total de Saques: R$ {resultado['total_saques']:.2f}\n")
            arquivo.write(f"Saldo Final: R$ {resultado['saldo_final']:.2f}\n")

        print("Relatório gerado com sucesso!")

    except Exception as erro:
        print(f"Erro ao gerar relatório: {erro}")
