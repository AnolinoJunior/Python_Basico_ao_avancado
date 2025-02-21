for i in range(10):
    if i == 5:
        print('i é 3, pulando...')
        continue
    
    if i == 8:
        print('i é 8 , seu else não executará')
        break
    

    for j in range (1,5):
        print(i,j)
else:
    print('For completo com sucesso')    
