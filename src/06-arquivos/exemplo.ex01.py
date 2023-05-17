
 


def carregar_dados_alunos(arquivo_dados, dados):
        arquivo_dados = open('src/arquivo_dados.txt', 'r')
        dados=[]
        for dado in arquivo_dados:
            dados.append({"prontuario": dado[0], "nome": dado[1], "email": dado[2]})
            return tuple(dados)
        arquivo_dados.close()

print(dados)
carregar_dados_alunos(dados)

