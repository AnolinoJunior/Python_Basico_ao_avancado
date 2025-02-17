def pesquisa_binaria(lista, alvo) :

    IndiceMinimo = 0

    IndiceMaximo = len(lista) - 1

    ultimaPosicaoMeio = 0
    
    while IndiceMinimo <= IndiceMaximo :

        posicaodomeio = (IndiceMinimo + IndiceMaximo) // 2

        if lista [posicaodomeio] == alvo :

         return posicaodomeio

        if lista[posicaodomeio] > alvo :

           IndiceMaximo = posicaodomeio - 1
        else:
           IndiceMinimo = posicaodomeio + 1
          
        if  IndiceMinimo <= IndiceMaximo :
             ultimaPosicaoMeio = posicaodomeio

        if alvo > len(lista) - 1:
          return len(lista)     


        return ultimaPosicaoMeio

minha_lista = [1,3,5,6] 

print (pesquisa_binaria(minha_lista, 5)) # 2

print (pesquisa_binaria(minha_lista, 2)) # 1

print (pesquisa_binaria(minha_lista, 4)) # 4 