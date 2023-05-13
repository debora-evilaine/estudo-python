#crie uma função que recebe três números como parâmetro (n1, n2, n3) e imprime na saída padrão a soma dos números

n1, n2, n3 = float(input('Entre com o n1: ')), float(input('Entre com o n2: ')), float(input('Entre com o n3: '))
def somar(n1, n2, n3):
  soma = n1 + n2 + n3
  print('A soma dos números é:',soma)

somar(n1, n2, n3)