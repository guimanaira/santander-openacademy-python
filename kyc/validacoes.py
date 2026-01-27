from erros import IdadeInvalidaError, CPFInvalidoError, RendaInsuficienteError

def validar_idade(idade):
    if idade < 18:
        raise IdadeInvalidaError("Cliente deve ser maior de 18 anos")

def validar_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        raise CPFInvalidoError("CPF deve conter 11 números")

def validar_renda(renda):
    if renda < 2000:
        raise RendaInsuficienteError("Renda mínima exigida é R$ 2.000")