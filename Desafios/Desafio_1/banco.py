"""
fazer um sistema bancario com as seguintes funções
    trabalha apenas com um usuario
    todos os depositos sao armazenados em uma variavel e exibidos em extrato
    permite realizar 3 saques diarios
    com limite de 500R$ por saque
    caso n ter sado aparecer
    saques armazenados em um variavel para mostra me extrato
    NO FIM DEVE LISTRAR TODOS Os depositos e saques realizado na conta
    deve utulizar usando formato R$ xxx.xx
"""

menu = """
[d] depositar
[s] sacar
[e] extrato
[q] sair
==> """


saldo = 0
limite = 500
extrato = "" 
numer_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"deposito: R$ {valor:.2f}\n"

        else:
            print("operação falhou")

    elif opcao == "s":
        valor = float(input("informe o valor do sque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numer_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("vc n tem saldo suficiente")
        elif excedeu_limite:
            print("valor do saque excede o limite")
        elif excedeu_saques:
            print("excedeu o limite de saque diario")

        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n "

        else:
            print('operação falhou')

    elif opcao == "e":
        print("\n================== EXTRATO ================")
        print("não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {valor:.2f} ")
        print("\n================== EXTRATO ================")

    elif opcao == "q":
        break

    else:
        print("operação invalida")