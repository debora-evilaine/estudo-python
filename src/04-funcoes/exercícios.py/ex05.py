peso, altura = float(input('Entre com o seu peso: ')), float(input('Entre com a sua altura: '))

individuo ={
    'peso': peso,
    'altura': altura
}
imc = peso / (altura * altura)

resultados = []

def calcular_imc(*args):
    imc = peso / (altura * altura)
    print('O seu IMC é:',imc)
calcular_imc(peso, altura)

PESO_NORMAL= 18.5 < imc < 24.9
    
def obter_classificacao(*args):
    if imc > 0:
        if imc <= 18.5:
            resultados.append('Você está: abaixo do peso')
            
        elif 18.5 < imc < 24.9:
            resultados.append('Você está: com o peso normal')
            
        elif 25.0 < imc < 29.9:
            resultados.append('Você está: com excesso de peso')
            
        elif 30.0 < imc < 34.9:
            resultados.append('Você está: com obesidade de grau 1')
            
        elif 35.0 < imc < 39.9:
            resultados.append('Você está: com obesidade de grau 2')
            
        elif imc >= 40.00:
            resultados.append('Você está: com obesidade de grau 3')
    else:
        print('O IMC é muito baixo para um ser humano!')

obter_classificacao(imc)

def situacao_individuo(imc):
    if imc != PESO_NORMAL and imc <=18.5:
        resultados.append('e precisa: ganhar peso')
    elif imc != PESO_NORMAL and imc >=29.9:
        resultados.append('e precisa: perder peso')
    if imc == PESO_NORMAL:
        resultados.append('seu peso é normal')
situacao_individuo(imc)

print(*resultados)
 