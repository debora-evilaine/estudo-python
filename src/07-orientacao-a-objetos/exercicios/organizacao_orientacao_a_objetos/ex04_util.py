# primeiro passo: criar a classe Participacao com os atributos básicos:

class Participacao:
    def __init__(self, data_inicio, data_fim, aluno):
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        
    def __str__(self):
        return f'A data de início é {self.data_inicio}, a data final é {self.data_fim}, o aluno é {self.aluno}'


class Projeto:
    def __init__(self, codigo, titulo, responsavel, participacao):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel
        self.participacoes = [participacao]
        
    def add_participacao(self, particpacao):
        self.participacoes.append(particpacao)
    
    # agora temos que exibir essa lista:
    def exibir_a_lista(self):
        print(f'Os dados se referem ao projeto de: {self.responsavel}')
        for participacao in self.participacoes:
            print(participacao)
        

    def __str__(self):
        return f'O código é {self.codigo}, o projeto é {self.titulo}, o responsável é {self.responsavel}'




    
    