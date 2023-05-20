
import ex02_util
            
with open('/home/evildeb/estudo-python/src/06-arquivos/exercicios/arquivo_projetos.txt', 'r', encoding = 'utf-8') as real:
    ex02_util.carregar_dados_alunos(real)