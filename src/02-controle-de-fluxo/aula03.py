""" Aula 03 - loop for"""

# É usado para repetir instruções e iterar elementos

linguagens = ['c', 'python', 'java']
for i in range(len(linguagens)):
        print(linguagens[i])

# TEMPLATE DE FOR PARA PYTHON:
# for valor in coleção:
        # instrução 
# o operador in tem comportamentos diferentes a depender do contexto 

#for linguagem in linguagens:
        #print(linguagem.upper())




nota1 = 10.0
nota2 = 5.5
nota3 = 8.3

notas = [10.0, 5.5, 8.3]
soma = 0.0
for nota in notas:
        soma = soma + nota

média = soma / len(notas)
print(média)

# range
valores = range(0, 10, 2)
# o zero é o início do range, o 10 é o fim do range e o 2 é o step (de quanto em quanto o range pula)
print(valores)
for valor in valores:
        print(valor)

# valores = range(10, 0, -1) : os números estão indo de cima para baixo, começando em 9 até 0
# quando é assim, é preciso acrescentar o step em -1, pois o range está decrementando de 1 em 1

