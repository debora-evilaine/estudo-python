""" Aula 03 - Tipos de dados - Sets (conjuntos)"""

# Características do sets:
# não são ordenados, mutáveis (podem ser editadas)
#  não indexáveis (não acessáveis por index)
# não aceitam elementos duplicados

# criar um set:

numeros = {1, 5, 7, 4, 3, 3, 1}
print(numeros, type(numeros)) 

for numero in numeros:
    print(numero)

print(3 in numeros)
print(50 in numeros)

 # adicionar itens ao set: método add
 #append: ideia de adicionar no final
 #insert: ideia de adicionar em uma posição
print(numeros)
numeros.add(8)
print(numeros)

# adicionar elementos de um set em outro:
numeros2 = {1,5,2,2,4,9}
numeros.update(numeros2)
print('------')
print(numeros)
print(numeros2)
print(numeros, type(numeros))