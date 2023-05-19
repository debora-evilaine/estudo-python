""" Aula 02: atributos de instância e de classe """
class Pessoa:
    especie = 'Humano' # esse é um atributo de classe, pois todos os objetos criados nessa classe terão esse valor
    def __init__(self, nome, email): # os atributos de instância nesse caso são: nome e email
        self.nome = nome
        self.email = email
        
pessoa1 = Pessoa('Maria da Silva', 'maria@email.com')
pessoa2 = Pessoa('João dos Santos', 'joao@email.com')
pessoa3 = Pessoa('Pedro da Silva', 'pedro@email.com')
pessoa1.especie = 'Alienígena' # mudamos o atributo de especia da pessoa1, mas isso não afeta o atributo de classe da classe Pessoa ou o objeto pessoa2o

Pessoa.especie = 'Alienigenas do passado' # agora, todos os objetos recebem um novo atributo, 
#exceto pelo objeto pessoa1, que ainda tem o seu atributo exclusivo


print(pessoa1.nome, pessoa1.email, pessoa1.especie)
print(pessoa2.nome, pessoa2.email, pessoa2.especie) # aqui, acessamoso atributo de classe "especie" diretamente pelo objeto pessoa1
print(Pessoa.especie) # aqui, acessamos o atributo de classe "especie" diretamente através da classe Pessoa
print(pessoa3.nome, pessoa3.email, pessoa3.especie)