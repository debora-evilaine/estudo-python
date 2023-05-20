"""Aula 01 - módulos e pacotes"""
# from uteis import fatorial, dobro ( você até pode fazer assim, mas não é recomendado pois
# pode gerar conflitos dentro do python)

import numeros

num = int(input('Digite o valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')


