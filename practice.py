lista = ['Ana', 'João', 'Pedro']

nome_inorreto = input('Digite o nome incorreto: ')
nome_correto = input('Digite o nome correto: ')

if nome_inorreto in lista:
    idx = lista.index(nome_inorreto)
    lista[idx] = nome_correto
    print(f'{nome_inorreto} foi substituido por {nome_correto}')
    print(lista)
else:
    print(f'{nome_inorreto} nao localizado, tente novamente.')