def pesquisa_binaria(lista, item):
        baixo = 1
        alto = len(lista) - 1
        while baixo <= alto: 
            meio = (baixo + alto) // 2 
            chute = lista[meio]
            if chute == item: 
                return meio
            if chute > item: 
                alto = meio -1
            else: 
                baixo = meio + 1

        return None 

minha_lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40] 

print (pesquisa_binaria(minha_lista, 33))
print (pesquisa_binaria(minha_lista,3))