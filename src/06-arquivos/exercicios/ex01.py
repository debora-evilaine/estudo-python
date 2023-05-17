
def carregar_dados_alunos(arquivo):
    dados = []
    for linha in arquivo.readlines():
        linha = linha.split(',')
        dados.append(linha)
        
    dados_totais=[]
    
    for dado in dados:
        dados_totais.append({'prontuario': dado[0], 'nome': dado[1], 'email': dado[2]})
        return tuple(dados_totais)
    print(dados_totais)
            
with open('arquivo_de_dados.txt', 'r') as arquivo:
    carregar_dados_alunos(arquivo)