import ex02_util

# terceiro passo: criar objeto "projeto"
projeto1 = ex02_util.Projeto(20, 'Laboratório de Desenvolvimento de Software','Pedro Gomes')
projeto2 = ex02_util.Projeto(20, 'Laboratório de Química', 'Emanuel de Souza')

# checando se os projetos são os mesmos...
if projeto1.codigo == projeto2.codigo:
    print('Os projetos são os mesmos!')
else:
    print(projeto1)
    print(projeto2)

    
    