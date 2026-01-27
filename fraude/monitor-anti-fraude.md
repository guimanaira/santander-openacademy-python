# 🔍 Monitor de Movimentações Suspeitas (Anti-Fraude) 


## 🚀 Desafio

O desafio consiste em **aplicar conceitos intermediários de Python para desenvolver um sistema simples de monitoramento de transações financeiras**, simulando um **processo básico de detecção de movimentações suspeitas (Anti-Fraude)** utilizado por bancos e instituições financeiras.

A aplicação analisa transações registradas em arquivo CSV e identifica comportamentos fora do padrão, como **valores elevados**, **horários incomuns**, **tentativas excessivas de login** e **inconsistências entre saldo e valor da transação**.


## 🎯 Objetivo Geral

- Desenvolver um monitor simples de movimentações suspeitas em transações financeiras.
- Identificar transações com valores acima do limite esperado.
- Detectar transações realizadas em horários incomuns.
- Verificar inconsistências entre saldo disponível e valor da transação.
- Analisar múltiplas tentativas de login como indicativo de risco.
- Registrar alertas de fraude em arquivo de log para auditoria.



## 🤖 Ferramentas e Conceitos Aplicados

- **Python**
- Leitura de arquivos CSV
- Manipulação de datas e horários (`datetime`)
- Funções
- Estruturas condicionais (`if / else`)
- Listas e conjuntos (`list`, `set`)
- Escrita de logs em arquivos
- Organização de código em módulos
- Simulação de regras de negócio antifraude



## 🧠 Processo de Criação

O projeto foi estruturado de forma modular para garantir **clareza, organização e escalabilidade**, simulando boas práticas utilizadas em sistemas de monitoramento financeiro.

- Leitura e tratamento de dados de transações a partir de um arquivo CSV
- Definição de regras simples de risco baseadas em valor, horário, saldo e comportamento
- Criação de funções específicas para análise de fraude
- Utilização de conjuntos para validação de canais permitidos
- Registro de transações suspeitas em arquivo de log
- Separação entre lógica de análise e execução principal do sistema



## 📁 Estrutura do Projeto

```
fraude/
│── transacoes.csv           # Base de dados com transações financeiras
│── monitor.py               # Regras de análise e detecção de fraude
│── main.py                  # Execução principal do monitor
│── fraude.log               # Registro das transações suspeitas

```


## 💻 Projeto

[Monitor de Movimentações Suspeitas (Anti-Fraude)](https://github.com/guimanaira/santander-openacademy-python/tree/main/fraude)
