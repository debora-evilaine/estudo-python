

def linha_para_dict(linha):
    lista_dados = ['prontuario', 'nome', 'email']
    dicio1 = {
		    'prontuario': 'SP000001',
		    'nome': 'Maria da Silva',
		    'email': 'maria@email.com'
	  }
    
    dicio2 = {
		    'prontuario': 'SP000002',
		    'nome': 'Pedro Gomes',
		    'email': 'pedro@email.com'
     }
    
    dicio3 = {
		    'prontuario': 'SP000003',
		    'nome': 'João Santos',
		    'email': 'joao@email.com'
    }

    linha = int(input('Entre com o valor da linha: '))
    if linha == 0:
        print(dicio1, f'Os dados se referem à lista:{lista_dados}')
    elif linha == 1:
        print(dicio2, f'Os dados se referem à lista:{lista_dados}')
    else:
        print(dicio3,f'Os dados se referem à lista:{lista_dados}' )
    

with open('/home/evildeb/estudo-python/src/06-arquivos/exercicios/arquivo_de_dados.txt', 'r', encoding = 'utf-8') as arquivo:
    linha_para_dict(arquivo)