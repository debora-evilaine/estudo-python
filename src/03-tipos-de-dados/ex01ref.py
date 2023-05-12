

print('Entre com os três números: ')
numeros = [input('') , input('') , input('')]

numeros_convertidos = []
for numero in numeros:
    numeros_convertidos.append(float(numero))

POSSIBILIDADE1 = numeros_convertidos[2] > numeros_convertidos[1] > numeros_convertidos[0] 
POSSIBILIDADE2 = numeros_convertidos[1] > numeros_convertidos[2] > numeros_convertidos[0]
POSSIBILIDADE3 = numeros_convertidos[2] > numeros_convertidos[0] > numeros_convertidos[1]
POSSIBILIDADE4 = numeros_convertidos[1] > numeros_convertidos[0] > numeros_convertidos[2]
POSSIBILIDADE5 = numeros_convertidos[0] > numeros_convertidos[2] > numeros_convertidos[1]
POSSIBILIDADE6 = numeros_convertidos[0] > numeros_convertidos[1] > numeros_convertidos[2]
POSSIBILIDADE7 = numeros_convertidos[0] == numeros_convertidos[1] == numeros_convertidos[2]

possibilidade = []
if POSSIBILIDADE1:
    possibilidade.append(float(numeros_convertidos[2]))
    possibilidade.append(float(numeros_convertidos[0]))    
    print(f'O maior número é: {numeros_convertidos[2]} e o menor número é: {numeros_convertidos[0]}')
      
elif POSSIBILIDADE2:
    possibilidade.append(float(numeros_convertidos[1]))
    possibilidade.append(float(numeros_convertidos[0]))    
    print(f'O maior número é: {numeros_convertidos[1]} e o menor número é: {numeros_convertidos[0]}')


elif POSSIBILIDADE3:
    possibilidade.append(float(numeros_convertidos[2]))
    possibilidade.append(float(numeros_convertidos[1]))    
    print(f'O maior número é: {numeros_convertidos[2]} e o menor número é: {numeros_convertidos[1]}')

elif POSSIBILIDADE4:
    possibilidade.append(float(numeros_convertidos[1]))
    possibilidade.append(float(numeros_convertidos[2]))    
    print(f'O maior número é: {numeros_convertidos[1]} e o menor número é: {numeros_convertidos[2]}')

elif POSSIBILIDADE5:
    possibilidade.append(float(numeros_convertidos[0]))
    possibilidade.append(float(numeros_convertidos[1]))    
    print(f'O maior número é: {numeros_convertidos[0]} e o menor número é: {numeros_convertidos[1]}')

if POSSIBILIDADE6:
    possibilidade.append(float(numeros_convertidos[0]))
    possibilidade.append(float(numeros_convertidos[2]))    
    print(f'O maior número é: {numeros_convertidos[0]} e o menor número é: {numeros_convertidos[2]}')
    
if POSSIBILIDADE7: 
    print('Os números são iguais!')


