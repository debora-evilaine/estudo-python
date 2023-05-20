# primeiro passo: criar classe aluno com os valores básicos
# Nenhum dos atributos pode ser vazio ou nulos (utilizar propriedades).

class Aluno:
    def __init__(self, prontuario, nome, email):
        self.prontuario = prontuario
        self.nome = nome
        self.email = email

    @property
    def prontuario(self):
        return self._prontuario 
    

    @prontuario.setter
    def prontuario(self, value):
        if value is None or value == '':
            raise ValueError('O campo "prontuario" não pode ser vazio ou nulo!!')
        self._prontuario = value
        
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, value):
        if value is None or value =='':
            raise ValueError('O campo "nome" não pode ser vazio ou nulo!!')
        self._nome = value
        
    @property
    def email(self):
        return self._email
        
    @email.setter
    def email(self, value):
        if value is None or value == '':
            raise ValueError('O campo "email" não pode ser vazio ou nulo!!')
        self._email = value
    
        
    def __str__(self):
        return f'O aluno tem o prontuario {self.prontuario}, o nome {self.nome} e o email {self.email}'




    
    
    
    
    
