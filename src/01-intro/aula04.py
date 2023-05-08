""" Aula 04 - variáveis, constantes e literais"""

#as variáveis são containers para guardar dados
numero = 10
print(numero, type(numero))

#é possível alterar o valor de uma variável
numero = 20
print(numero)

#também é possível fazer múltiplas atribuições
nome, idade, endereco = 'maria', 20, 'rua das ...'
print(nome, idade, endereco)

nome = 'maria'
idade = 20
endereco = 'rua das...'

print(nome, idade, endereco)

#é possível, ainda, atribuir o mesmo valor a variáveis diferentes:
nome1 = nome2 = nome3 = 'João'
print(nome1, nome2, nome3)

nome2 = 'pedro'
print(nome1, nome2, nome3)

#variáveis
#snake_case
id_funcionario = 209
salario_atual = 5000.50
print(id_funcionario, salario_atual)

#constantes
#UPPERCASE
PI = 3.14
MAIORIDADE_CIVIL = 21
MAIORIDADE_PENAL = 18
print(PI, MAIORIDADE_CIVIL, MAIORIDADE_PENAL)

#literais
idade = 27
print(idade)
print(27)

#numericos
print(10, type(10))
print(-10, type(-10))
print(10.50, type(10.50))

#string
print('maria', type('maria'))
print("maria", type("maria"))
print("john's house")
print('o filme estava "excelente"')

#booleano
print(True, type(True))
print(False, type(False))

#coleções

#lista
numeros = [1, 2, 3]
print(numeros, type(numeros))

#tupla
emails = ('joao@email', 'maria@email')
print(emails, type(emails))

#conjunto
nomes = {'maria', 'joao', 'pedro', 'maria'}
print(nomes, type(nomes))

#dicionário
aluno = {
    'prontuario' : 1234,
    'nome': 'maria da silva',
    'idade': 34
}

print(aluno, type(aluno))


