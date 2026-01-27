from analise import(
    ler_clientes,
    filtrar_inadimplentes,
    gerar_lista_cobranca
)

CAMINHO_ARQUIVO = "clientes.csv"

def main():
    clientes = ler_clientes(CAMINHO_ARQUIVO)
    inadimplentes = filtrar_inadimplentes(clientes)

    print(f"Total de cliente: {len(clientes)}")
    print(f"Clientes inadimplentes: {len(inadimplentes)}")


    gerar_lista_cobranca(inadimplentes)
    print("Listas de cobrança gerada com sucesso!")

if __name__ == '__main__':
    main()