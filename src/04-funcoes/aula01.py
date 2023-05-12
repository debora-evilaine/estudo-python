"""Aula 01 - introdução às funções"""

# função é um bloco que realiza uma tarefa específica
# para dividir um problema em pequenas partes
# auxilia a evitar a duplicação de códigos

# existem funções chamadas de standard library functions/ built-in functions
# não são definidas, só usadas
# ex: print, len()

# e as user defined functions, que são as funções que nós definimos 
# para que elas façam parte da solução do problema que estamos resolvendo

# declarar uma função:

# declaração
# nome
# parâmetros
# retorno
def saudacoes():
    print('Olá')

# chamar a função:
saudacoes() #pode chamar a função quantas vezes quiser
saudacoes()
saudacoes()
saudacoes()



# a função abaixo imprime 'Olá, x' sendo que x é o nome colocado pelo usuário
# podemos chamar valores, variáveis e expressões para chamar uma função
nome = input('Entre com o seu nome:')
def saudacoes(nome):    
    print(f'Olá, {nome}')

saudacoes(nome) # nome é um parâmetro, e pode haver quantos parâmetros você quiser

# declaração
# nome
# parâmetros
# retorno
def calcular_media (numero1, numero2, numero3):
    media = (numero1 + numero2 + numero3) / 3
    print(media)

# chamada da função
# argumentos são literais

calcular_media (10.0, 6.0, 3.0)
n1 = 10.0
n2 = 6.0
n3 = 3.0
# argumentos são variáveis
calcular_media(n1, n2, n3)

# agora, vamos fazer uma função que ao invés de imprimir (print) o valor de média,
# ela retorna esse valor, e então podemos decidir se damos print ou outra coisa

def calcular_media (numero1, numero2, numero3):
    media = (numero1 + numero2 + numero3) / 3
    return media

media = calcular_media(5.0, 2.3, 9.1) / 3
print('Valor da média', media)

# aqui, ao invés de darmos print, poderíamos ter enviado a média por email
# ou salvar no banco de dados, ou salvar no arquivo

