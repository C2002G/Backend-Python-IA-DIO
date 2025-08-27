class Estacionamento:
    vaga = "esta estacionado"

    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        return f"{self.modelo} - {self.ano} - {self.vaga}"
    

def mostrar_carros_estacionados(*objs):
        for obj in objs:
            print(obj)

carro_1 = Estacionamento("Focus", 2008)
carro_2 = Estacionamento("Fiat", 2010)
carro_3 = Estacionamento("Onix", 2009)

print(carro_1)
print(carro_2)
print(carro_3)

carro_2.ano = 2009

mostrar_carros_estacionados(carro_1, carro_2, carro_3)