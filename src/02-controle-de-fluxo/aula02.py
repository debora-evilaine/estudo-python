""" Aula 02 - instrução if"""

# TEMPLATE DO IF NO PYTHON:
 # if condição
        #instrução
        #instrução
        #instrução
# a identação é o que indica se a instrução está dentro ou fora do if
#nessa linha, por exemplo, por não estar identada, ela está FORA do if

valor_desconto = 15.0
DESCONTO_ESPECIAL = valor_desconto >= 20.0

if DESCONTO_ESPECIAL:
        print('Desconto especial!')
else: 
        print('Sem desconto especial!')    

# Nome tem que ter pelo menos 3 caracteres

nome = 'Loi'

print(len(nome), type(nome))

NOME_INVALIDO = len(nome) < 3

if NOME_INVALIDO:
        print('Nome deve ter pelo menos 3 caracteres!')
else:
        print('Nome válido!')


NOME_VALIDO =len(nome) >= 3

if NOME_VALIDO:
        print('Nome válido!')
else:
        print('Nome inválido!')

if not NOME_INVALIDO:
        print('Nome válido!')
else:
        print('Nome inválido!') 

        # nome tem que ter pelo menos 3 caracteres
        # idade tem que ser maior ou igual a 18
        # exibir todos os erros no final, apenas

nome = 'los'
idade = 18
erros = []

NOME_INVALIDO = len(nome) < 3

if NOME_INVALIDO:
        erros.append('Nome deve ter pelo menos 3 caracteres!')

IDADE_INVALIDA = idade < 18
if IDADE_INVALIDA:
        erros.append('Idade deve ser maior ou igual a 18')

if len(erros) != 0:
        print(erros)
else:
        print('Dados válidos!')

# o python avalia true or false da seguinte maneira:
# False: False, None, 0, 0.0, string vazia ' ', lista, tupla, set vazia
#True: todas as outras instâncias
# isso significa dizer que não é necessário adicionar o len(erros) ao último if, 
# pois como a sua lista está vazia, o python já o considera como False

# if, elif, else

# verifica se um número é positivo ou negativo ou zero
numero = 3

if numero > 0:
        print('Positivo!')

elif numero == 0:
        print('Numero igual a zero!')
else:
        print('Negativo!')

# Calcule a média e verifique se as duas notas são válidas antes do cálculo

n1 = 5.3
n2 = 10.0

NOTA1_VALIDA = 0 <= n1 <= 10
NOTA2_VALIDA = 0 <= n2 <= 10

if NOTA1_VALIDA and NOTA2_VALIDA:
        media = (n1 + n2) / 2
        if media >= 6:
                print('Aprovado!')
        elif media >=4:
                print('Recuperação')
        else:
                print('Reprovado!')
else:
        print('Notas inválidas!')


