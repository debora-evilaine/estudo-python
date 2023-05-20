# primeiro passo: criar classe aluno com os valores básicos
# Nenhum dos atributos pode ser vazio ou nulos (utilizar propriedades).
import ex01_util

aluno1 = ex01_util.Aluno('SP0101', 'João da Silva', 'joao@email.com')
aluno2 = ex01_util.Aluno('9', 'Maria da Silva', 'maria@email.com')

# comparando se os alunos são iguais ou diferentes.....

if aluno1.prontuario == aluno2.prontuario:
    print('Os alunos são a mesma pessoa!')
    
else: 
    print(aluno1)       
    print(aluno2)
    
    
    
    
    
    
