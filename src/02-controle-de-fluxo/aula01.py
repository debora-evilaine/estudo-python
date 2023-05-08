""" Aula 01 - Operadores"""

# operadores aritméticos

n1 = 10.2
n2 =3.5
resultado = n1 + n2 + 8.5
print('1 + 1', 1 + 1, type(1 + 1))
print('1.2 + 1.3', 1.2 + 1.3, type(1.2 + 1.3))
print('resultado', resultado, type(resultado))
print(3-2)
print(3*2, type(3*2))
print(3/2, type(3/2))
print(3%2)
print(10 // 3)
print(10 ** 2)

# Operador de atribuição

x = 10.0 #o valor 10.0 foi atribuído à variável x
print(x)

# Operadores de comparação ou relacionais

resultado = x > 10
print(resultado, type(resultado))

print('10 == 10', 10 == 10, type(10 == 10))
print('10 != 10', 10 != 10, type(10 != 10))
print('10 > 10', 10 > 10, type(10 > 10))
print('10 >= 10', 10 >= 10, type(10 >= 10))
print('10 < 10', 10 < 10, type(10 < 10))
print('10 <= 10', 10 <= 10, type(10 <= 10))

#condicao = x > 10 and resultado < 3.0
#if condicao: 

# Operadores lógicos

print('True and True', True and True, type(True and True)) #And é severo: o resultado só é True somente quando os dois elementos são True
print('True and False', True and False, type(True and False))
print('False and True', False and True, type(False and True))
print('False and False', False and False, type(False and False))

print('True or True', True or True, type(True or True)) #Or é bonzinho: o resultado só será falso quando ambos os elementos forem falsos
print('True or False', True or False, type(True or False))
print('False or True', False or True, type(False or True))
print('False or False', False or False, type(False or False))

condicao = True
print('not de condicao:', not condicao, type(not condicao))

# Operadores especiais do python:

#is
# == compara se dois valores são iguals
# is: verifica se duas variáveis apontam para o mesmo lugar na memória

a = 10
b = 10.0
c = b

print(a == b, b == c, a == c)
print(a is b, b is c, a is c) # b is c é True porque o c está apontando para b, enquanto que 
#a não aponta para b, e b não aponta para a, nem a aponta para c




#in
# o in busca um elemento específico em strings, listas, tuplas, conjuntos e dicionários

frase = 'Você é um palavrão!'
print('palavrão' in frase, type('palavrão' in frase)) # ele retorna True, pois existe a palavra
#"palavrão" dentro da frase (in frase)

numeros = [1, 5, 2, 6]
print(1 in numeros) # verifica se há o número 1 em numeros, retornando True porque há sim.

pessoa = {
    #nome é uma chave, assim como idade e email!
    'nome': 'Maria',
    'idade': 22,
    'email': 'maria@email.com'
}

print('nome' in pessoa) # o in não trabalha sobre os resultados da chave, mas sim sobre a chave em si
# isso significa dizer que o in retorna false para 'Maria', 22 e 'maria@email.com', porque
#eles não são as chaves do dicionário