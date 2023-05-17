
def carregar_dados_alunos(arquivo):
    dados = []
    for linha in arquivo.readlines():
        linha = linha.split(',')
        dados.append(linha)
        
    dados_totais=[]
    
    for dado in dados:
        dados_totais.append({'codigo': dado[0], 'título': dado[1], 'responsável': dado[2]})
        return tuple(dados_totais)
    print(dados_totais)
            
with open('arquivo_projetos.txt', 'r', encoding='utf-8') as arquivo:
    carregar_dados_alunos(arquivo)