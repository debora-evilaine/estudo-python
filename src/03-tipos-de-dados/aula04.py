""" Aula 04 - Tipos de dados - Dicionários"""

# Características do dicts:
# não são ordenados, mutáveis (podem ser editadas)
#  não indexáveis (não acessáveis por index)
# não aceitam elementos duplicados

#coleção de key-value
# a key é única, ou seja, sem keys duplicadas no dic
# é mutável

# criar um dict:
carro = {
    "marca": "ford",
    "modelo": "mustang",
    "ano": 1964

}
print(carro, type(carro))

# resgatar valores:

print(carro["marca"])
# ou:
print(carro.get("marca"))

# pegar todas as chaves:

print(carro.keys())

# pegar todos os valores:

print(carro.values())

# pegar tudo junto:

print(carro.items())

# verificar se existe uma chave específica:

print("marca" in carro)

# adicionar chaves ou valores de forma dinâmica
carro["cor"] = "Azul"
print("cor" in carro)
print(carro, type(carro))

# retirar keys do dict:

#carro.pop("marca")
#print(carro)

# remover a key mas dar print do valor:

marca = carro.pop("marca")
print(marca)
print(carro)

# loop
for key in carro:
    print(key, carro[key], type(key))

for value in carro.values():
    print(value)

for key in carro.keys():
    print(key)

for key, value in carro.items():
    print(key, value)

# lista de dicionários
aluno1 = {
    "nome": "joao",
    "email": "joao@gmail.com",
    "notas": [10, 2.3, 7]
}

aluno2 = {
    "nome": "maria",
    "email": "maria@gmail.com",
    "notas": [10, 5, 1]
}

alunos = [aluno1, aluno2]
for aluno in alunos:
    print(aluno['nome'], aluno['email'], aluno['notas'])
    for nota in aluno["notas"]:
        print(nota)