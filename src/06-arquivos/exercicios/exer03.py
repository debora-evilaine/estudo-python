from ex01 import carregar_dados_alunos


def lista_para_dict(arquivo):
    lista_para_dicionario = ['prontuario', 'nome', 'email']
    dados_totais = []
    for linha in lista_para_dicionario:
        for linha in ex01:
            linha = linha.split()
            dados_totais.append(linha)
            print(dados_totais)

with open ('/home/evildeb/estudo-python/src/06-arquivos/exercicios/ex01.py', 'r' , encoding='utf-8') as total:
    lista_para_dict(total)






