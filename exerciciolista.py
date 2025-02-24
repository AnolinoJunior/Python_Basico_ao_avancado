import os

lista_adicionavel = []

while True:

    print('Selecione uma opção')
    entrada_indices = input ('[i]nserir [a]pagar [l]istar: ')
    
    if entrada_indices == 'i':
        os.system('clear')
        entrada_inserir = input ('Valor: ')
        lista_adicionavel.append(entrada_inserir)

    elif entrada_indices == 'a':
        entrada_apagar = input ('Escolha o indice do ITEM: ')
        entrada_apagar = int(indices)
        del lista_adicionavel[indices]

    elif entrada_indices == 'l':
        os.system('clear')

        if len(lista_adicionavel) == 0 :
            print('nada na lista')  

    indices = range(len(lista_adicionavel)) 
    for indices in indices :
        print(indices,lista_adicionavel[indices])
    
    else:
        print('por favor siga as instruções')
    



