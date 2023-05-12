""" Aula 01 - Tipos de dados - Listas"""

# Características da lista:
# ordenadas, mutáveis (podem ser editadas) e indexáveis (acessáveis por index)

# Criação de lista:
nomes = ['Maria', 'Pedro', 'João']
print(nomes, type(nomes))

# Formas de acessar elementos da lista
print(nomes[0])
print(nomes[0:2])  # Não inclui a última posição, que é João
print(nomes[:2])
print(nomes[0:])  # imprime todas as posições
print(nomes[1:])  # imprime do 1 até a posição final

# Modificar elementos:

nomes[0] = 'Maria da Silva'
nomes[1:] = 'Pedro da Silva', 'João Santos'
print(nomes)

# Tamanho de uma lista: função len
tamanho = len(nomes)
print(tamanho)

# adicionar elementos na lista: método append
nomes.append('Marta Gomes')
print(nomes)

# adicionar elementos em uma posição específica da lista: método insert
nomes.insert(0, 'Ghuilherme Tavares') # adiciona guilherme tavares na posição zero, e deslocou os
#outros elementos para a próxima posição
print(nomes)

nomes.insert(2, 'Ana Lucia') 
print(nomes)

# adicionar elementos de uma outra lista: método extend
nomes2 = ['Kaio Silva', 'Carlos Gomes']
print(len(nomes))
nomes.extend(nomes2)
print(len(nomes))
print(nomes)

# remover elementos de uma lista: método remove
nomes.remove('Maria da Silva')
print(nomes)

# ou:

# método del (de deletar)
#remove da memória
del nomes[0]
print(nomes)

# limpar a lista: método clear
#nomes.clear()
#print(nomes)

# iteração em lista
for nome in nomes:
    print(nome)

for i in range(len(nomes)):
    print(nomes[i])