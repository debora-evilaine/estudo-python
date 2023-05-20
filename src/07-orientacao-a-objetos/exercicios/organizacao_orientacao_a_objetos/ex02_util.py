# primeiro passo: criar a classe com os atributos básicos

class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel
        
        
# segundo passo: impossibilitar a entrada de campos vazios ou nulos usando as properties
    @property 
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, value):
        if value is None or value =='':
            raise ValueError('O campo "codigo" não pode ser vazio ou nulo!')
        self._codigo = value
        
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, value):
        if value is None or value =='':
            raise ValueError('O campo "titulo" não pode ser vazio ou nulo!!')
        self._titulo = value 
        
    @property
    def responsavel(self):
        return self._responsavel
    
    @responsavel.setter
    def responsavel(self, value):
        if value is None or value =='':
            raise ValueError('O campo "responsavel" não pode ser vazio ou nulo!')
        self._responsavel = value 
        
        
# quarto passo: criar f string para representar os objetos 
    def __str__(self):
        return f'O código é {self.codigo}, o projeto é {self.titulo} e o responsável é {self.responsavel}'


    
    