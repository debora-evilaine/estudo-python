""" Aula 05 - Tipos de dados"""
#numericos
#int, float

idade = 20
peso = 70.6

print(idade, type(idade))
print(peso, type(peso))

#strings

nome = pedro
sobrenome = dos santos
nome_completo = nome + ' ' + sobrenome
print(nome_completo)

produto = coca-cola

printf(f'O cliente {nome} {sobrenome} comprou o produto {produto}')


print(nome[0], nome[-1])

print(nome.lower())
print(nome.upper())
print(nome, sobrenome)

#boolean
print(True, type(True))

resultado = 10 < 3
print(resultado, type(resultado))

#listas
frutas = ['bananas', 'uvas' 'morangos']
print(frutas)
print(frutas[0])
print(frutas[1])
print(frutas[2])
#uma lista sempre começa contando do zero

frutas[0]= 'banana nanica'
frutas.append('abacaxi')
print(frutas)
print(len(frutas)) #diz quantos valores exitem em fritas

for fruta in frutas:
    print(fruta.upper())

    #trupla
    codigos = ('SP01', 'SP02', 'SP03')
    print(codigos[0]) #a tupla não suporta a adição de valores
print(len(codigos))

#conjuntos
resultado_sorteio = {10, 4, 3, 55 , 9}
print(resultado_sorteio)

resultado_sorteio.add(23)
print(resultado_sorteio)

#dicionários
funcionario = {
    'codigo': 123,
    'nome': 'Maria'
    'salario': 12348
}
print(funcionario['codigo'])
print(funcionario['Maria'])
print(funcionario['salario'])

print(funcionario.keys())
print(funcionario.values())

funcionario['salario'] = 9000
print(funcionario)