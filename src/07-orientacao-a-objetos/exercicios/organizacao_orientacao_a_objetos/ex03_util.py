#crie uma classe Participacao que deve ter como 
#atributos codigo, data inicio, data fim, aluno e o projeto associado. 

# primeiro passo: criar a classe com os atributos básicos

class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto_associado):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto_associado = projeto_associado
# terceiro passo: criar f string para a representação do objeto ficar mais bonita
    def __str__(self):
        return f'O codigo do projeto é {self.codigo}, a data de início é {self.data_inicio}, a data de término é {self.data_fim}, o aluno é {self.aluno} e o projeto é {self.projeto_associado}'
        
#segundo passo: criar objeto aluno

