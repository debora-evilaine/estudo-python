def carregar_dados_alunos(arquivo):
    dados = []
    for linha in arquivo.readlines():
        linha = linha.split(',')
        dados.append(linha)
        
    
    
    for dado in dados:
        dados_totais=[]
        dados_totais.append({'codigo': dado[0], 'título': dado[1], 'responsável': dado[2]})
        print(dados_totais)