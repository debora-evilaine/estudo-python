def copa_do_mundo_titulos(pais, *args):
    print('País: ', pais)
    for titulo in args:
        print('ano: ', titulo)

copa_do_mundo_titulos('Brasil', '1958', '1962', '1970', '1994', '2002')

copa_do_mundo_titulos('Brasil', '1958', '1962', '1970', '1994', '2002')

copa_do_mundo_titulos('Espanha', '2010')

def calcule_preco(valor, **kwargs):
    imposto = kwargs.get('imposto')
    desconto = kwargs.get('desconto')
    if imposto:
        valor += valor * (imposto / 100)
    if desconto:
        valor -= desconto
    return valor
    
preco_final = calcule_preco(100.0)
print(preco_final)

preco_final = calcule_preco(100.0, desconto=5.0)
print(preco_final)

preco_final = calcule_preco(100.0, imposto=7)
print(preco_final)

preco_final = calcule_preco(100.0, imposto=7, desconto=5.0)
print(preco_final)