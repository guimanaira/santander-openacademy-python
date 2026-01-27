from validacoes import validar_idade, validar_cpf, validar_renda
from erros import IdadeInvalidaError, CPFInvalidoError, RendaInsuficienteError

try:
    idade = int(input("Digite sua idade: "))
    cpf = input("Digite seu CPF (apenas números): ")
    renda = float(input("Digite sua renda mensal: "))

    validar_idade(idade)
    validar_cpf(cpf)
    validar_renda(renda)

    print("✅ Cadastro aprovado com sucesso!")

except IdadeInvalidaError as e:
    print(f"❌ Erro de idade: {e}")

except CPFInvalidoError as e:
    print(f"❌ Erro de CPF: {e}")

except RendaInsuficienteError as e:
    print(f"❌ Erro de renda: {e}")

except ValueError:
    print("❌ Digite apenas números para idade e renda")
