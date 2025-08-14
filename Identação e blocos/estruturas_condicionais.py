"""
# if e else
saldo = 2000.0
saque = float(input("informe o valor do saque: "))


if saldo >= saque:
    print("realizado o saque")
else:
    print("valor insuficiente")

# if,else,elif
opcao = int(input("informe uma ipção: [1]Sacar/[2]extrato "))

if opcao == 1:
    valor = float(input("informe o valor do saque"))
elif opcao == 2:
    print("exibindo extrato")
else:
    SystemExit("opcção invalida")
"""

# aninhado

conta_normal = True
conta_universtitaria = False

saldo = 2000
saque = input("digite seu valor de saque: ")
cheque = 450


if conta_normal:
    if saldo >= saque:
        print("saque realizado com sucesso")
    elif saque <= (saldo + cheque):
        print("saque feito com ajuda do cheque")
    else:
        print("saldo insuficente")
elif conta_universtitaria:
    if saldo >= saque:
        print("saque realizado")
    else:
        print("saldo insuficiente")
else:
    print("sistema n encontrado")


#   TERNARIO
x = 10
print ("par" if x % 2 == 0 else "impar")
   
saldo = 2000
saque = 2500

status = 'Sucesso!' if saldo >= saque else 'Falha!'