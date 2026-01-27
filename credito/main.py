from score import calcular_score
from simulador import analisar_credito

def main():
    renda = float(input("Informe sua renda mensal: "))
    dividas = float(input("Informe o total de dívidas: "))

    historico = input("Seu histórico de pagamento é bom? (s/n): ").lower()
    historico_bom = historico =="s"

    score, classificacao = calcular_score(renda, dividas, historico_bom)
    resultado = analisar_credito(score, classificacao)

    print("\n📊 Resultado da Análise de Crédito")
    print(f"Score calculado: {score}")
    print(f"Classificação: {classificacao}")
    print(f"Decisão: {resultado}")

if __name__ == "__main__":
    main()
