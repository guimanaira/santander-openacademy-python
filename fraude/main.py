import csv
from monitor import verificar_fraude, registrar_log

def ler_transacoes():
    with open("transacoes.csv", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        return list(leitor)

def main():
    transacoes = ler_transacoes()

    for transacao in transacoes:
        alertas = verificar_fraude(transacao)

        if alertas:
            registrar_log(transacao["TransactionID"], alertas)
            print(f"Fraude detectada na transação {transacao['TransactionID']}")

if __name__ == "__main__":
    main()
