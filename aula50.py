'''
Métodos úteis:
    append - Adiciona um item ao final da lista
    insert - Adicona um item no índice escolhido
    pop    - Removo do final ou do índice escolhido
    del    - Apaga um índice
    clear  - Limpa a lista 
    extend - Estende a lista
    + - concatena listas
'''
#       0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(100, 5)
print(lista[3])

