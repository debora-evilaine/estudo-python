""" Aula 04: propriedades """

# as propriedades são uma forma de controlar o acesso aos atributos de um objeto
# formas personalizadas de mudar ou "controlar" os métodos de um objeto

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    # essa property é uma getter
    @property
    def base(self):
        return self._base  
    
    # essa é a setter da getter
    @base.setter
    def base(self, value):
        if value <= 0.0:
            raise ValueError('A base deve ser maior do que zero')
        self._base = value
    
    # getter da altura  
    @property
    def altura(self):
        return self._altura
    
    # setter da altura
    @altura.setter
    def altura(self, value):
        if value <= 0.0:
            raise ValueError('A altura deve ser maior do que zero')
        self._altura = value
        
        
    @classmethod
    def from_list(cls, lista):
        return cls(lista[0], lista[1])
    
    @classmethod
    def from_str(cls, rep_retangulo):
        base, altura = rep_retangulo.split(sep = ',') 
        return cls (float(base) , float(altura))
        
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
        
        
retangulo1 = Retangulo(4, 0)


retangulo1.base = 7 # o setter e o getter me garantiram que não vai ser possível criar um retangulo com base igual ou menor a 0
retangulo1.altura = 9
print(retangulo1.base)

        
        
        