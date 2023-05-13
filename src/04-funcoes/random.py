altura, peso = input('Entre com o seu peso: '), input('Entre com a sua altura: ')

individuo ={
    'altura': altura,
    'peso': peso
}
imc = 0
resultados = []

def calcular_imc(individuo):
    imc = peso / altura * altura
    print(imc)

""" abaixo_do_peso = imc < 18,5
peso_normal = 18,5 < imc < 24, 9
excesso_de_peso = 25,0 < imc < 29,9
obesidade_tipo1 = 30,0 < imc < 34, 9
obesidade_tipo2 = 35,0 < imc < 39,9
obesidade_tipo3 = imc >= 40,00
    
def obter_classificacao(imc):
    if abaixo_do_peso:
        resultados.append(imc)
    elif peso_normal:
        resultados.append(imc)
    elif excesso_de_peso:
        resultados.append(imc)
    elif obesidade_tipo1:
        resultados.append(imc)
    elif obesidade_tipo2:
        resultados.append(imc)
    elif obesidade_tipo3:
        resultados.append(imc)

def situacao_individuo(imc):
    if imc < peso_normal:
        resultados.append('ganhar peso')
    elif imc > peso_normal:
        resultados.append('perder peso')
    else:
        resultados.append('peso normal')

print(resultados)


        

        
    
    




    
    
 """