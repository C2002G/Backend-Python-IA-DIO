salario = 2000


def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


fds = salario_bonus(500)  # 2500
print(fds)