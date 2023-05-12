

print('Entre com os três números: ')
numeros = [input('') , input('') , input('')]
print('A lista de números em string é: ',numeros, type(numeros))

numeros_convertidos = []
for numero in numeros:
    numeros_convertidos.append(float(numero))
print('A lista de números em float é: ',numeros_convertidos, type(numeros_convertidos))    

print('--------')

possibilidade = []
if numeros_convertidos[2] > numeros_convertidos[1] > numeros_convertidos[0]:
    possibilidade.append(float(numeros_convertidos[2]))
    possibilidade.append(float(numeros_convertidos[0]))    
    print(f'O maior número é: {numeros_convertidos[2]} e o menor número é: {numeros_convertidos[0]}')
      
elif numeros_convertidos[1] > numeros_convertidos[2] > numeros_convertidos[0]:
    possibilidade.append(float(numeros_convertidos[1]))
    possibilidade.append(float(numeros_convertidos[0]))    
    print(f'O maior número é: {numeros_convertidos[1]} e o menor número é: {numeros_convertidos[0]}')


elif numeros_convertidos[2] > numeros_convertidos[0] > numeros_convertidos[1]:
    possibilidade.append(float(numeros_convertidos[2]))
    possibilidade.append(float(numeros_convertidos[1]))    
    print(f'O maior número é: {numeros_convertidos[2]} e o menor número é: {numeros_convertidos[1]}')

elif numeros_convertidos[1] > numeros_convertidos[0] > numeros_convertidos[2]:
    possibilidade.append(float(numeros_convertidos[1]))
    possibilidade.append(float(numeros_convertidos[2]))    
    print(f'O maior número é: {numeros_convertidos[1]} e o menor número é: {numeros_convertidos[2]}')

elif numeros_convertidos[0] > numeros_convertidos[2] > numeros_convertidos[1]:
    possibilidade.append(float(numeros_convertidos[0]))
    possibilidade.append(float(numeros_convertidos[1]))    
    print(f'O maior número é: {numeros_convertidos[0]} e o menor número é: {numeros_convertidos[1]}')

if numeros_convertidos[0] > numeros_convertidos[1] > numeros_convertidos[2]:
    possibilidade.append(float(numeros_convertidos[0]))
    possibilidade.append(float(numeros_convertidos[2]))    
    print(f'O maior número é: {numeros_convertidos[0]} e o menor número é: {numeros_convertidos[2]}')
    
if numeros_convertidos[0] == numeros_convertidos[1] == numeros_convertidos[2]: 
    print('Os números são iguais!')


