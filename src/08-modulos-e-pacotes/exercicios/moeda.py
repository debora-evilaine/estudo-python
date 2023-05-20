import programa_moeda

n = float(input('Digite o valor: '))
aumento = float(input('Entre com o aumento: '))
diminui = float(input('Entre com a cominuição: '))


print(f'O aumento é: {programa_moeda.moeda(programa_moeda.aumentar(n, aumento))}')

print(f'A diminuição é: {programa_moeda.moeda(programa_moeda.diminuir(n, diminui))}')

print(f'O dobro é: {programa_moeda.moeda(programa_moeda.dobro(n))}')

print(f'A metade é: {programa_moeda.moeda(programa_moeda.metade(n))}')
