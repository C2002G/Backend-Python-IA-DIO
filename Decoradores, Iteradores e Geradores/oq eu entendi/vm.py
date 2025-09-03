"""def calcular(operacao):
    def somar(a,b):
        return a + b

    def subtrair(a,b):
        return a - b

    if operacao == "+":
        return somar
    else:
        return subtrair


resultado = calcular("+")(2, 2)
print(resultado)
"""


def frufru(funcao):
    def mostrar(*args, **kwargs):
        print("em cima")
        funcao(*args, **kwargs)
        print("em baixo")

    return mostrar


@frufru
def ola_mundo(nome, idade, sexp):
    print(f"ola mundo! {nome} {idade} {sexp}")


ola_mundo("Gabriel", "23", "Masculino")
