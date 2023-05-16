""" Aula 06 - Arquivos"""

# open("caminho", "r")

# a função open recebe dois caminhos, e o segundo pode ser divido em cinco outros módulos:
# r = leitura
# a = append (incrementar)
# w = escrita
# x = criar arquivo
# r+ = leitura e escrita 

arquivo = open("src/06-arquivos/teste.txt", "r")

print(arquivo.readable())


arquivo.close()
