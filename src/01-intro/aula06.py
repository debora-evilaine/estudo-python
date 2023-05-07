""" Aula 06 - conversão de tipos"""

# Conversão implícita

leitura = 5.53
peso = 3
total = leitura * peso
print(total, type(total))

#conversão explícita, ou type casting

soma = 13.4 + float('3.5')
print(soma, type(soma))

idade = int('32')
print(idade, type(idade))

nome = 'maria'
altura = 1.70
mensagem = nome + ' tem a altura de ' + str(altura)

print(mensagem)
