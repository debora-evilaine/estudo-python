notas = '1 2 3 4 5'
listas = notas.split(' ')

print(listas)
print('------')

reais = []
for elemento in listas:
    reais.append(float(elemento))
print(reais)

soma = 0
for real in reais:
    soma = soma + real
    media = soma / len(reais)
print('A média do aluno é:', media)
if media >= 6:
    print('Aluno aprovado!')
elif media >= 4:
    print('Recuperação')
else:
    print('Reprovado')

   