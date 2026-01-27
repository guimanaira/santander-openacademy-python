# 🧩 Pipeline Simples de Dados Bancários (Estilo ETL)

## 🚀 Desafio

O desafio consiste em **simular um pipeline simples de dados bancários no estilo ETL (Extract, Transform, Load)**, aplicando conceitos intermediários de Python para reproduzir um fluxo muito comum em ambientes de **engenharia de dados, analytics e sistemas financeiros**.
A aplicação realiza a **extração de dados a partir de um arquivo CSV**, aplica **transformações para geração de métricas financeiras** e finaliza com a **carga dos resultados em um relatório estruturado**, simulando um processo real de consolidação de informações utilizado por bancos e instituições financeiras.



## 🎯 Objetivo Geral

- Simular um pipeline de dados bancários no modelo ETL.
- Extrair dados financeiros a partir de arquivos CSV.
- Transformar dados brutos em informações consolidadas.
- Calcular métricas financeiras como total de depósitos, total de saques e saldo final.
- Gerar um relatório final estruturado a partir dos dados processados.
- Demonstrar organização de código e separação de responsabilidades.



## 🤖 Ferramentas e Conceitos Aplicados

- **Python**
- Leitura e escrita de arquivos
- Manipulação de arquivos CSV
- Funções
- Módulos
- Estruturas condicionais
- Estruturas de dados (`list`, `dict`)
- Tratamento de exceções (`try / except`)
- Organização de pipeline de dados (ETL)


## 🧠 Processo de Criação

O projeto foi desenvolvido seguindo o conceito de **pipeline de dados**, com cada etapa isolada em um módulo específico, garantindo **clareza, organização e facilidade de manutenção**.

- Criação do módulo de **extração**, responsável por ler e validar os dados de entrada.
- Implementação do módulo de **transformação**, onde são aplicadas regras de negócio e cálculos financeiros.
- Desenvolvimento do módulo de **carga**, responsável por gerar o relatório final.
- Criação de um arquivo principal para **orquestrar todo o fluxo ETL**.
- Tratamento de exceções para garantir maior robustez do sistema.

Essa abordagem reflete boas práticas utilizadas em projetos reais de dados e engenharia.


## 📁 Estrutura do Projeto

```
etl_banco/
│── extracao.py           # Responsável pela extração dos dados (E)
│── transformacao.py      # Responsável pela transformação e cálculos (T)
│── carga.py              # Responsável pela geração do relatório final (L)
│── main.py               # Orquestração do pipeline ETL
│── dados.csv             # Fonte de dados bancários
│── relatorio_final.txt   # Resultado do processamento
```


## 💻 Projeto

[Pipeline Simples de Dados Bancários (Estilo ETL)](https://github.com/guimanaira/santander-openacademy-python/tree/main/etl_banco)
