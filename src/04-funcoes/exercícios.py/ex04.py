# crie uma função que recebe vários argumentos numéricos através do *args retorna a soma dos números



def soma(*args):
    somar = 0
    for arg in args:
        somar = somar+ arg
    print(somar)
    
soma(1,2,3,4,5)