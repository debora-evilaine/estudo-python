""" input and output de dados"""

#saída padrão sys stdout
print('Hello world', 'Maria', 1, True, sep='@', end='\n')

arquivo = open('nomes.txt', 'w', encoding='utf-8')

print('joao@email.com', 'maria@email.com', 'pedro@email.com', file=arquivo, sep=';')

#entrada
#input
#nome=input('Digite seu nome: ')
#idade = int('Digite sua idade ')
#if idade>=18qqq
#print({nome}, você é maior de idade!)
#else 
#print({nome}, você é menor de idade!)

#file
arquivo_notas = open('notas.txt', 'r', enconding='utf-8')
conteudo = arquivo_notas.read()
notas = conteudo.split(sep=';')
print(notas)
notas=[float(nota) for nota in notas]
print(notas)

media = notas[0] + notas[1] + notas[2] / len(notas)
print(media)


