

print('Entre com o ID:')
id = input('')
if len(id) != 7:
    print('ID inválido!')
elif id[0] != 'B' or id[1] != 'R' or id[6] != 'X':
    print('ID inválido!')
elif id[2] == '0' and id[3] == '0' and id[4] == '0' and id[5] == '0':
    print('ID inválido!')
else:
    print('ID válido!')




