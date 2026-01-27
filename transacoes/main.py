from analise import ler_transacoes, calcular_resumo

def main():
    caminho = "dados_transacoes.csv"

    transacoes = ler_transacoes(caminho)

    if not transacoes:
        print("Nenhuma transação encontrada.")
        return
    
    entradas, saidas, saldo = calcular_resumo(transacoes)

    print("RESUMO FINANCEIRO")
    print(f"Total de entradas: R$ {entradas:.2f}")
    print(f"Total de saídas: R$ {saidas:.2f}")
    print(f"Saldo final: R$ {saldo:2.f}")

if __name__ == "__main__":
    main()