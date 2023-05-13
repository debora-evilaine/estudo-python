id = input('Entre com o ID:')
ID_INVALIDO1 = len(id) != 7
ID_INVALIDO2 = id[0] != 'B' or id[1] != 'R' or id[6] != 'X'
ID_INVALIDO3 = id[2] == '0' and id[3] == '0' and id[4] == '0' and id[5] == '0'

problemas = []

if ID_INVALIDO1 :
    problemas.append(f'O ID informado {id} não possui sete dígitos')
    
elif ID_INVALIDO2:
    problemas.append(f'O ID informado {id} não começa com BR ou termina com X')

elif ID_INVALIDO3:
    problemas.append(f'O ID informado {id} possui todos os numerais iguais a zero')
else:
    print('ID válido!')

print(*problemas)