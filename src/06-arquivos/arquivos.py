# # para abrir um arquivo primeiro é necessário criar uma variável qualquer para poder 
# # atribuir a função 'open' dentro dela. nesse caso, a variável qualquer é "arq"


# arq = open('arquivo.txt', 'w')
# x = ['Caio', 'Marcos', 'João']




# #arq.write('Olá, tudo bem?')# espera uma única string

# # arq.writelines(x) # podemos fazer isso de outra forma, como vemos abaixo, caso a lista não
# # tenha '\nº':

# for nome in x:
#     arq.write(nome + '\n')



# arq.close()

# #arq.writelines  # espera uma quantidade de iteráveis diversa de strings como em uma lista, por exemplo



# PORÉM, há uma maneira mais eficiente e recomendada de abrir arquivos, sem utilizar o 
#.open e .close. fazemos dessa forma:

# with open('arquivo.txt', 'w') as arq:
#     arq.write('teste')

# print('fim') # esse printf está fora da identação do with, ou seja, está fora do contexto do
# arquivo, então o arquivo está fechado 

# with open('arquivo.txt', 'a') as arq:
#     arq.write('\ndébora')

# print('fim')

# with open('arquivo.txt', 'r') as arq:
#     x = arq.read()
#     print(x, type(x)) # o type de x é uma string, porque read lê a string e devolve uma string

# with open('arquivo.txt', 'r') as arq:
#     x = arq.readlines()
#     print(x, type(x)) # o type de x aqui é uma lista, pois readlines devolve uma lista

# with open('arquivo.txt', 'rb') as arq:
#     x = arq.read()
#     print(type(x.decode())  # devolve x em bytes, e não em string, é útil para mandar o código para alguém
# o decode transformou o x em string 

# with open('arquivo.txt', 'r') as arq:
#     for i in arq:
#         print(i) 

with open('arquivo.txt', 'r') as arq:
    print(next(arq))
    print(next(arq))