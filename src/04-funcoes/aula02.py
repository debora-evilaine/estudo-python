"""Aula 02 - arguments; positional, keyword, default value"""

# declarar uma função que soma dois números

def soma(n1, n2):
  return n1 + n2

def dividir(dividendo, divisor):
  return dividendo / divisor

# isso se chama argumentos posicionais, pois está passando
# o argumento 2 ao n1 e o 3 ao n2
print(soma(2, 3))
print(dividir(10.0, 2.0))

# argumentos nomeados (keywords)

print(soma(n1=3.0, n2=6.3))
# ou:
print(soma(n2=3.0, n1=6.3))
print(dividir(divisor = 2, dividendo = 10))

# unpack de list 
numeros = [10.0, 5.5]
print('Somar números com uma lista:',soma(numeros[0], numeros[1]))
print('Somar números com uma lista:',soma(*numeros)) # unpack

# unpack com tuple
numeros = (10.0, 5.5)
print('Somar números com uma lista:',soma(numeros[0], numeros[1]))
print('Somar números com uma lista:',soma(*numeros)) # unpack

# unpack de dict
numeros = {
  "n1": 2,
  "n2": 5.3
}
print('Somar números com um dict:',soma(**numeros)) # unpack com 2 asteriscos, pois queremos unpack dos values e não das keys

# default values:
def saudacoes(nome, saudacao='oi'): #agora oi tem um default value de 'oi'
  return f'{saudacao} {nome}'

print(saudacoes('joão', 'olá'))
print(saudacoes('maria', 'bom dia'))
print(saudacoes('maria'))

print(saudacoes(saudacao = 'oi oi', nome ='márcio'))
print(saudacoes(nome ='márcio'))