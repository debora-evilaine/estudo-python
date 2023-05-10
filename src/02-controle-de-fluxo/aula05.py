""" Aula 05 - break e continue"""

# normalmente usadas dentro de um loop

for i in range(10):
    if i == 4:
        break
    print(i)

    #encontrar a posição de um número em uma lista de inteiros
    #caso não encontre, a posição é igual a -1

    busca = 5
    numeros = [1, 4, 9, 7, 5, 3, 2, 1, 7]
    posição = -1
    contador = 0

    for numero in numeros:
        if numero == busca:
            posição = contador
            break
        contador +=1

print(posição)

# continue
# pula a iteração atual, e não para o loop que nem o break

for numero in numeros:
    if numero == 3:
        continue
    print(numero)
    