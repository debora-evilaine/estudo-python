""" print('Entre com o ID:')
id = input('')
if len(id) != 7:
    print('ID inválido!')
    print('Identificador informado: ', id)
    print('Erros do identificador: não apesenta números inteiros entre 00')
elif id[0] != 'B' or id[1] != 'R' or id[6] != 'X':
    print('ID inválido!')
else:
    print('ID válido!') """

print('Entre com o ID:')
id = input('')
if len(id) != 7:
    print('ID inválido!')
    print('Identificador informado: ', id)
    print('Erros do identificador: não apesenta 7 dígitos')
elif id[0] != 'B' or id[1] != 'R' or id[6] != 'X':
    print('Identificador informado: ', id)
    print('ID inválido!')
    print('Erros do identificador: não começa com BR ou termina com X')
elif id[2] == '0' and id[3] == '0' and id[4] == '0' and id[5] == '0':
    print('ID inválido!')
    print('Identificador informado: ', id)
    print('Erros do identificador: não apesenta números inteiros entre 0001 e 9999')
else:
    print('ID válido!')
