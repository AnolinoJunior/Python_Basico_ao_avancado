'''faça um programa que peça o primeiro nome do usuario. se o nome tiver 4 letras ou 


menos escrava ''seu nome eh curto''; se tiver entre 5 e 6 letras, escrava


''seu nome eh normal'', maior que 6 escrava '' seu nome eh muito grande''.
'''
nome = input ('Digite seu nome:')
tamanho_nome = len(nome)

if tamanho_nome > 1 : 

    if tamanho_nome <= 4 :
        print('seu nome eh curto')
    if tamanho_nome >= 5 and tamanho_nome <= 6 :
        print('seu nome eh normal')
    else:
        print('seu nome eh muito grande')

    
else :
    print('Por favor, digite 1 numero')   