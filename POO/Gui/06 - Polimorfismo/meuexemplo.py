class Carro:
    def correr(self):
        print("vrum vrum")

class Onix(Carro):
    def correr(self):
         super().correr()
    
class Mustang(Carro):
    def correr(self):
        print("Musttang n corre, ele voa")

class skate(Carro):
    def correr(self):
        print('oia o flip')

def pista_corrida(obj):
    obj.correr()

c1 = Onix()
c2 = Mustang()



pista_corrida(c1)
pista_corrida(c2)
pista_corrida(skate())
