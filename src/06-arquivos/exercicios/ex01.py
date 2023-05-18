
def carregar_dados_alunos(arquivo):
    dados = []
    for linha in arquivo.readlines():
        linha = linha.strip()
        linha = linha.split(',')
        dados.append(linha)
    
   
    
    for dado in dados:
        dados_totais=[]
        dados_totais.append({'prontuario': dado[0], 'nome': dado[1], 'email': dado[2]})
        print(dados_totais)
            
with open('/home/evildeb/estudo-python/src/06-arquivos/arquivo_de_dados.txt', 'r', encoding = 'utf-8') as total:
    carregar_dados_alunos(total)



 


