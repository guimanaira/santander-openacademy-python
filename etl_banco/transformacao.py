def transformar_dados(dados):
    total_depositos = 0
    total_saques = 0

    for transacao in dados:
        valor = float(transacao["TransactionAmount"])
        tipo = transacao["TransactionType"]

        if tipo == "Credit":
            total_depositos += valor
        elif tipo == "Debit":
            total_saques += valor

    saldo_final = total_depositos - total_saques

    return{
        "total_depositos": total_depositos,
        "total_saques": total_saques,
        "saldo_final": saldo_final
    }
