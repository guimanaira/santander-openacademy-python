import csv

def ler_clientes(caminho_arquivo):
    clientes = []

    with open(caminho_arquivo, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=",")

        for linha in leitor:
            linha_normalizada = {
                chave.strip(): valor for chave, valor in linha.items()
            }
            clientes.append(linha_normalizada)

    return clientes

#Filtrar inadimplentes
def filtrar_inadimplentes(clientes):
    inadimplentes = []

    for cliente in clientes:
        if cliente["Status"].lower() == "inadimplente":
            inadimplentes.append(cliente)

    return inadimplentes

#Classificar Risco
def classificar_risco(score):
    score = int(score)

    if score < 500:
        return "Alto Risco"
    elif score < 700:
        return "Médio Risco"
    else: 
        return "Baixo Risco"
    
#Gerar lista para cobrança
def gerar_lista_cobranca (inadimplentes):
    with open("lista_cobranca.txt", "w", encoding="utf-8") as arquivo:
        for cliente in inadimplentes:
            risco = classificar_risco(cliente["Score"])

            arquivo.write(
                f"Nome: {cliente['Nome']} |"
                f"CPF: {cliente['CPF']} | "
                f"Valor: R$ {cliente['Valor Contratado']} |"
                f"Vencimento: {cliente['Data de Vencimento']} |"
                f"Risco: {risco}\n"
            )