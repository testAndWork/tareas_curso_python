num = []



def agregar_num(numero):
    num.append(numero)

def sum_num():
    sum_numero = 0
    for nota in num:
        sum_numero += nota
    print(sum_numero)