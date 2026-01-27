from relatorio import gerar_relatorio

def main():
    resultado = gerar_relatorio("dados.csv")

    if resultado is None:
        print("Nenhuma transação válida encontrada.")
        return
    

    print("RELATÓRIO BANCÁRIO DIÁRIO")
    print(f"Total de transações: {resultado["total_transacoes"]}")
    print(f"Valor total movimentado: R$ {resultado["valor_total"]:.2f}")
    print(f"Maior operação: R$ {resultado["maior_operacao"]:.2f}")
    print(f"Menor operação: R$ {resultado["menor_operacao"]:.2f}")


if __name__ == "__main__":
    main()