# 3️⃣ Simulador de Crédito e Score Simplificado

## 🚀 Desafio

O desafio consiste em **aplicar conceitos fundamentais e intermediários de Python para criar um simulador de crédito**, capaz de **calcular o score do cliente e decidir pela aprovação ou reprovação de crédito**, com base em critérios financeiros comuns no setor bancário.

A aplicação simula regras reais de análise de crédito, considerando **renda mensal**, **nível de endividamento** e **histórico financeiro**, além de classificar o cliente em faixas de score utilizadas pelo mercado.

📌 **A lógica de pontuação foi inspirada nas faixas do Serasa Score**, adaptadas para fins educacionais e de simulação.



## 🎯 Objetivo Geral

- Desenvolver um simulador de crédito simples e funcional
- Calcular o **score do cliente** com base em:
    - Renda mensal
    - Dívidas em relação à renda
    - Histórico financeiro
- Classificar o score em faixas:
    - **0 – 300** → Baixo
    - **301 – 500** → Regular
    - **501 – 700** → Bom
    - **701 – 1000** → Excelente
- Definir **aprovação ou reprovação de crédito**
- Simular regras de negócio aplicadas por instituições financeiras



## 📊 Critérios de Score (Baseado no Serasa Score)

| Faixa de Score | Classificação | Risco de Crédito |
| --- | --- | --- |
| 0 – 300 | Baixo | Alto risco |
| 301 – 500 | Regular | Risco moderado |
| 501 – 700 | Bom | Baixo risco |
| 701 – 1000 | Excelente | Muito baixo risco |

⚠️ *Este modelo é uma simulação educacional e não representa regras oficiais de instituições financeiras.*



## 🤖 Ferramentas e Conceitos Aplicados

- **Python**
- Terminal / Console
- Editor de código (VS Code)
- Funções
- Operadores lógicos e aritméticos
- Estruturas condicionais (`if / elif / else`)
- Módulos próprios
- Retorno de valores
- Organização de código em camadas



## 🧠 Processo de Criação

O projeto foi estruturado de forma modular, seguindo boas práticas de desenvolvimento:

- Criação de uma função responsável pelo **cálculo do score**
- Aplicação de pesos positivos e negativos conforme perfil financeiro
- Classificação automática do score em faixas de risco
- Implementação da lógica de **aprovação ou reprovação de crédito**
- Separação entre:
    - Cálculo do score
    - Simulação do crédito
    - Execução principal da aplicação

Esse fluxo simula como sistemas reais de crédito funcionam em bancos e fintechs.


## 📁 Estrutura do Projeto

```
credito/
│── score.py           # Cálculo e classificação do score
│── simulador.py       # Regras de aprovação/reprovação de crédito
│── main.py            # Execução principal do sistema

```

---

## 💻 Projeto

[Simulador de Crédito e Score Simplificado](https://github.com/guimanaira/santander-openacademy-python/tree/main/credito)
