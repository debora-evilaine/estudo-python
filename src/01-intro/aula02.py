""" Aula 02 - Keywords e identificadores"""

#existem palavras reservadas, chamadas keywords, que não podem ser usadas como nomes de variáveis, como: 
#True, False, None, and, import, lambda

#identificadores são os nomes de variáveis, funções e classes
#são case sensitive, não podem ter espaçoes em branco, caracteres especiais, e devem sempre
#começar com letra ou _

nome = 'Maria'
idade = 30
Nome = 'João'
nome_completo = 'Maria da Silva'

#é uma boa prática colocar nomes claros para as variáveis, isto é, nomes que a façam ser identificada facilmente

c = 10
contador = 10

s = 10 + 20
soma = 10 + 20

#as constantes devem ter letras maiúsculas

PI = 3.14
MAIORIDADE = 18
idade = 18

if idade>= MAIORIDADE:
    print('maior de idade')
else:
    print('menor de idade')