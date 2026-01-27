def calcular_score(renda, dividas, historico_bom):
    score = 200 #score base(todo cliente começa com algo)

    #Renda mensal (até 400 pontos)
    if renda >= 7000:
        score += 400
    elif renda >= 5000:
        score += 250
    elif renda >= 3000:
        score += 200
    elif renda >= 1500:
        score += 120
    else:
        score += 50

    #Comprometimento da renda (até -350 pontos)
    if renda == 0:
        comprometimento = 1 if dividas > 0 else 0
    else:
        comprometimento = dividas / renda

    if comprometimento > 0.5:
        score -= 350
    elif comprometimento > 0.35:
        score -= 200
    elif comprometimento > 0.2:
        score -= 100

    #Histórico de Pagamento (até +- 250 pontos)
    if historico_bom:
        score += 250
    else:
        score -= 200

    #Classificação fina de score
    if score <= 300:
        classificacao = "Baixo"
    elif score <= 500:
        classificacao = "Regular"
    elif score <= 700:
        classificacao = "Bom"
    else:
        classificacao = "Excelente"

    return score, classificacao
