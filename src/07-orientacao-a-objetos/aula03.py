""" Aula 03: métodos de classe """

# usamos para criar objetos de maneora diferente

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    @classmethod # indica que o método abaixo é de classe, e não de instância
    def from_list(cls, lista): # cls é a classe em que método está, nesse caso, Retangulo
        return cls(lista[0], lista[1])
    
    @classmethod
    def from_str(cls, rep_retangulo):
        base, altura = rep_retangulo.split(sep = ',') # o split transformou cada elemento da string em lista
        return cls (float(base) , float(altura))
        
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
 

retangulo1 = Retangulo(10.0, 5.0) 
retangulo2 = Retangulo(6.0, 3.0)
retangulo3 = Retangulo.from_list([20.0, 3.5])
retangulo4= Retangulo.from_str('55.4, 13.5')

print(retangulo3.base, retangulo3.altura, retangulo3.calcular_perimetro(), retangulo3.calcular_area())      

print(retangulo4.base, retangulo4.altura, retangulo4.calcular_perimetro(), retangulo4.calcular_area())      

