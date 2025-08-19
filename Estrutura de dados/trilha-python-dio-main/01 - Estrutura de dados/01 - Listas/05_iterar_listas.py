carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)


for vaga, carro in enumerate(carros):
    print(f"{vaga}: {carro}")
