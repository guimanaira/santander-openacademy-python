from datetime import datetime

VALOR_MAXIMO = 10000
HORARIO_SUPEITO_INICIO = 0
HORARIO_SUPEITO_FIM = 5

#Função para verificar fraude
def verificar_fraude(transacao):
    alertas = []

    valor = float(transacao["TransactionAmount"])
    saldo = float(transacao["AccountBalance"])
    tentativas = int(transacao["LoginAttempts"])
    canal = transacao["Channel"]

    data = datetime.strptime(transacao["TransactionDate"], "%Y-%m-%d %H:%M:%S")
    hora = data.hour

    if valor > VALOR_MAXIMO:
        alertas.append("Valor muito alto")

    if hora >= HORARIO_SUPEITO_INICIO and hora <= HORARIO_SUPEITO_FIM:
        alertas.append("Transação em horário incomum")

    if valor > saldo:
        alertas.append("Saldo insuficiente")

    if tentativas >= 3:
        alertas.append("Muitas tentativas de login")

    canais_validos = {"APP", "WEB", "ATM"}
    if canal not in canais_validos:
        alertas.append("Canal desconhecido")

    return alertas

#Criação de logs de fraude
def registrar_log(transacao_id, alertas):
    with open("fraude.log", "a", encoding="utf-8") as log:
        log.write(f"Transação {transacao_id} suspeita:\n")
        for alerta in alertas:
            log.write(f" - {alerta}\n")
        log.write("\n")
       
