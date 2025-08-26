class Carro:
    def __init__(self, nome,):
        print("carro ligador")
        self.nome = nome
        

    # def __del__(self):
    #     print("terminando registro")

    def andar(self):
        print("carro  esta adnando")

    def buzinar(self):
        print("carro esta buzinando")

    def parar(self):
        print("carro esta parando")



classic = Carro("Classic 2008")
classic.andar()
classic.buzinar()
classic.parar()

print("novo carro chegou")
