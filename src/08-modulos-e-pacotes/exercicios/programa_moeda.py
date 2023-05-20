
def aumentar(n=0, aumento=0):
    res = n + aumento
    return res


def diminuir(n=0, diminui=0):
    res = n - diminui
    return res

def dobro(n=0):
    res = n * 2
    return res

def metade(n=0):
    res = n / 2
    return res 

def moeda(n = 0, moeda ='R$'):
    return f'{moeda}{n:.2f}'.replace ('.', ',')
