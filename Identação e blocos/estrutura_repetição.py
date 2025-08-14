texto = input("informe um texto: ")
VOAGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOAGAIS:
        print(letra, end="")
else:
    print()  # quebra linha
    print("feito")


#  RANGE
for numero in range(0, 11):
    print(numero, end="")

# tabuada

# start, fim, step
for numero in range(0, 51, 5):
    print(numero, end=" ")  # end para ser lado a lado


# while
opcao = -1

while opcao != 0:
    opcao = int(input('[1] sacar / [2] extrato / [0] sair'))


    if opcao == 1:
        print('sacando... ')
    elif opcao == 2:
        print('exbindo extrato')
else:
    print('obrigado por ser nosso cliente')

#break
opcao = -1

while True:
    numero = int(input('informe um numero: '))

    if numero == 10:
        break

    print (numero)