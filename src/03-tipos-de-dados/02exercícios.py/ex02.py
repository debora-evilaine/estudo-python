meses_do_ano = {
    1: "janeiro",
    2: "fevereiro",
    3: "março",
    4: "abril",
    5: "maio",
    6: "junho",
    7:"julho",
    8: "agosto",
    9: "setembro",
    10: "outubro",
    11: "novembro",
    12: "dezembro"

}
resultado = ''
mes = int(input('Entre com o número do mês: '))
if mes <= 0 or mes >= 13:
    print('Esse mês não existe!')
else:
    resultado = meses_do_ano[mes]
print(resultado)
        
        
