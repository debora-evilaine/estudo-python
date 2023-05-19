""" Aula 01 Introduçao à orientação a objetos"""

# é uma forma de se resolver um problema

# primeiro, vamos resolver um problema sem orientação a objetos:

# calcular a área e o perímetro de um retangulo:
#precisamos de uma estrutura para armazenar os dados do cálculo

retangulo1 = {
'base': 10.0,
'altura': 5.0
}

retangulo2 = {
'base': 6.0,
'altura': 3.0
}

# agora, realizamos os cálculos com funções

def calcular_area(retangulo):
    return retangulo['base'] * retangulo['altura']

def calcular_perimetro(retangulo):
    return 2 * (retangulo['base'] + retangulo['altura'])

print (calcular_area(retangulo1))
print(calcular_area(retangulo2))

print (calcular_perimetro(retangulo1))
print(calcular_perimetro(retangulo2))

# o código funciona, porém é mais interessante resolvermos esse problema com a orientação a objetos
# vamos fazer isso agora:

class Retangulo:
    def __init__(self, base, altura): # esse é o construtor
        #self.base = 10.0 
        #self.altura = 5.0 
        # esses atributos acima dizem que cada objeto terá esses atributos
        # mas essa não é a maneira mais correta de fazer
        
        self.base = base
        self.altura = altura
        # acima, você vê a maneira correta de fazer essa atribuição
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
    # acima, você vê os métodos
        


retangulo1 = Retangulo(10.0, 5.0) # aqui estamos criando objetos do tipo Retangulo
retangulo2 = Retangulo(6.0, 3.0) # não esqueça de colocar os parênteses, porque eles chamam o construtor de Retangulo
# o construtor cria os objetos em si
print(type(retangulo1), retangulo1)
print(type(retangulo2), retangulo2)

print(retangulo1.base, retangulo1.altura, retangulo1.calcular_area(), retangulo1.calcular_perimetro())
print(retangulo2.base, retangulo2.altura, retangulo2.calcular_area(), retangulo2.calcular_perimetro())

# acima, fizemos o seguinte:
# printamos a base e altura dos triangulos
# depois chamamos os métodos de calcular área e perímetro
# e printamos esses cálculos também






