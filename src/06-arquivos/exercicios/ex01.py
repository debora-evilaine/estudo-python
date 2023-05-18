
def carregar_dados_alunos(arquivo):
    dados = []
    for linha in arquivo.readlines():
        linha = linha.split(',')
        dados.append(linha)
        print(linha)
    dados_totais=[]
    
    for dado in dados:
        dados_totais.append({'prontuario': dado[0], 'nome': dado[1], 'email': dado[2]})
        return tuple(dados_totais)
    print(dados_totais)
            
with open('src/06/arquivos/arquivo_de_dados.txt', 'r', encoding = 'utf-8') as dados_totais:
    carregar_dados_alunos(dados_totais)



 


