

comprimento, altura, largura = float(input('Entre com o comprimento: ')), float(input('Entre com a altura: ')), float(input('Entre com a largura: '))
volume = (comprimento * altura * largura) / 1000
temperatura_ambiente = 0
temperatura_desejada = 0
potencia = volume * 0.05 * (temperatura_desejada - temperatura_ambiente)
filtragem = volume * 2.05
resultados= []

def volume_aquario(*args):
    volume = (comprimento * altura * largura) / 1000
    print('O volume é: ', volume)
    resultados.append(f'No total, temos que o volume é: {volume},')
volume_aquario(comprimento, altura, largura)


temperatura_desejada, temperatura_ambiente = float(input('Entre com a temperatura desejada: ')), float(input('E com a temperatura ambiente: '))

def potencia_aquario(*args):
    potencia = volume * 0.05 * (temperatura_desejada - temperatura_ambiente)
    print('A potência é: ', potencia)
    resultados.append(f'a potência é: {potencia}')
potencia_aquario(volume, temperatura_desejada, temperatura_ambiente)

def filtragem_aquario(*args):
    filtragem = volume * 2.05
    print('A filtragem é:', filtragem)
    resultados.append(f'e a filtragem é: {filtragem}')
filtragem_aquario(volume)

print(*resultados)
