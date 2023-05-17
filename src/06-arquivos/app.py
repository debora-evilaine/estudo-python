""" Aula 06 - Arquivos"""

# open("caminho", "r")

# a função open recebe dois caminhos, e o segundo pode ser divido em cinco outros módulos:
# r = leitura
# a = append (incrementar) 
# w = escrita
# x = criar arquivo
# r+ = leitura e escrita 

#arquivo = open("src/06-arquivos/teste3.txt", "x")

#print(arquivo.readable()) # verifica se o arquivo pode ser lido
#print(arquivo.read()) # a função read retorna todo o arquivo

#print(arquivo.readline()) # lê a primeira linha do arquivo
#print(arquivo.readline())
#print(arquivo.readline())
#print(arquivo.readline())
#print(arquivo.readline())

# lista = arquivo.readlines() # transforma o conteúdo do arquivo em uma lista, que pode ser manipulada
# print(lista)

# print(lista[3])

#arquivo.write("python\n")
# arquivo.write("c++\n")
# arquivo.write("terrafore\n")

#arquivo.close()

# DELETAR ARQUIVOS:
# para fazer isso, é preciso importar uma biblioteca do python chamada: os
# se o arquivo não estiver fechado, você não consegue deletá-lo

import os

# if os.path.exists("src/06-arquivos/teste2.txt"): # para saber se o arquivo existe
#     os.remove("src/06-arquivos/teste2.txt") # vai remover o arquivo teste3 da pasta 06-arquivos
# else:
#     print('esse arquivo não existe!')

# DELETAR PASTAS:

os.rmdir("src/06-arquivos/nova_pasta") # só remove a pasta se ela estiver vazia
# ou seja, para remover uma pasta cheia primeiro é necessário remover os arquivos dela e 
# DEPOIS deletá-la




