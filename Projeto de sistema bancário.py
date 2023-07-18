#Projeto de sistema bancário
menu = """

[d] depositar
[s] sacar
[e] extrato
[q] sair

=>"""

saldo = 1500.00
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("depósito")
        valor = float(input("Insira a quantia que deseja depositar: "))
        if valor > 0:
            saldo = saldo + valor
            print(f"o valor de R${valor:.2f} foi inserido em sua conta, o saldo atual é R${saldo:.2f}")
            print("Deseja realizar mais alguma operação em sua conta?")
            extrato += f"depósito de R${valor:.2f}\n"
        else:
            print("ERRO: valor inválido inserido, tente novamente")
    
    elif opcao == "s":
        print("saque")
        quantia = float(input("Insira a quantia que deseja sacar: "))
        if saldo >= quantia and quantia <= 501 and numero_saques < LIMITE_SAQUES:
            saldo = saldo - quantia
            numero_saques = numero_saques + 1
            print(f"O valor de R${quantia:.2f} foi sacado de sua conta, o saldo atual é R${saldo:.2f}.")
            extrato += f"saque de R${quantia:.2f}\n"

        elif numero_saques == LIMITE_SAQUES:
            print("Infelizmente você atingiu o limite de saques de hoje, por favor tente novamente outro dia.")

        elif quantia >= limite:
            print("ERRO: valor minimo de saque permitido apenas R$500")
            
    elif opcao == "e":
        if extrato == "":
            print("Nenhum extrato foi realizado no momento")
        else:
            print("extrato da conta:")
            print(f"{extrato}")

    elif opcao == "q":
        print("Obrigado, volte sempre")
        break
    
    else:
        print("Opção inválida, por favor insira o a operação desejada novamente.")