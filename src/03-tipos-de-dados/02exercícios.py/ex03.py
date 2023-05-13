meses_do_ano = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
meses = int(input('Entre com o número do mês: '))

if meses < 0 or meses >= 12:
    print('Esse mês não existe!')
else: 
    for mes in meses_do_ano:
        calendario = meses_do_ano[meses]
    print(calendario)