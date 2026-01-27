from conta import Conta
from excecoes import(
    SaldoInsuficienteError,
    LimiteExcedidoError,
    LimiteSaquesError,
    ValorInvalidoError
)

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

conta= Conta()

while True:
    opcao = input(menu)

    try:
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            conta.depositar(valor)
        
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            conta.sacar(valor)

        elif opcao == "e":
            conta.mostrar_extrato()

        elif opcao == "q":
            print("Saindo do sistema ...")
            break

        else:
            print("Operação inválida.")

    except(SaldoInsuficienteError,
           LimiteExcedidoError,
           LimiteSaquesError,
           ValorInvalidoError) as erro:
        print(f"Erro: {erro}")

    except ValueError:
        print("Erro: informe um valor numérico válido.")