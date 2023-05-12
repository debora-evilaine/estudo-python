""" Aula 02 - Tipos de dados - Tuplas"""

# Características da tupla:
# ordenadas, imutáveis (não podem ser editadas), ou seja, sem append ou index, por exemplo
# indexáveis (acessáveis por index)

# Criação de tupla:
nomes = ('Maria', 'Pedro', 'João')
print(nomes, type(nomes))

# acessar elementos da tupla
print(nomes[0])
print(nomes[0:2])  # Não inclui a última posição, que é João
print(nomes[:2])
print(nomes[0:])  # imprime todas as posições
print(nomes[1:])  # imprime do 1 até a posição final

# Modificar elementos: não é possível pois a tupla é imutável
# nomes[0] = 'Maria da Silva' = dá erro, pois a tupla não aceita mudança de valores
for nome in nomes:
    print(nome)

for i in range(len(nomes)):
    print(nomes[i])


nomes2 = 'Ana', 'Amélia', 'Marcos' #omitindo os parênteses
print(nomes2, type(nomes2))

# colocar o valor de tuplas em variáveis: 
# unpack
#nome1 = nomes2[0]
#nome2 = nomes2[1]
#nome3 = nomes2[2]
# acima foi feito SEM o unpack
# agora, com o unpack:

nome1, nome2, nome3 = nomes2
print(nome1, nome2, nome3)

# juntar duas tuplas: 
todos_nomes = nomes + nomes2
print(todos_nomes)

# COMO DECIDIR QUAL USAR??
# se preciso de ordenado e indexáveis: tupla ou lista
# se precisar ser imuntável: tupla
# se for mutável: lista
# portanto: depende do que você quer fazer!!

