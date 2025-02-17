'''
Faça um programa que peça ao usuario para digitar um numero inteiro,
informe se este numero eh par ou impar. caso o usario nao digite um nuero
inteiro, informe que nao eh um numero inteiro.
'''

entrada = input ('Digite um numero inteiro:')




if entrada.isdigit():


    entrada_int = int(entrada)


    par_impar = entrada_int % 2 == 0


    par_impar_texto = 'impar'



    if par_impar:


        par_impar_texto = 'par'



    print(f'o numero {entrada_int} eh {par_impar_texto}')


else:


    print('voce nao digitou um numero inteiro')





'''
Faça um programa que pergunte a hora ao usuario e, baseando-se no horario
descrito, exiba  a saudaçao apropriada, ex
bom dia 0-11, boa 12-17 e boa noite 18-23.
'''



'''faça um programa que peça o primeiro nome do usuario. se o nome tiver 4 letras ou 


menos escrava ''seu nome eh curto''; se tiver entre 5 e 6 letras, escrava


''seu nome eh normal'', maior que 6 escrava '' seu nome eh muito grande''.
'''




entrada = input ('Digite um numero inteiro:')




if entrada.isdigit():


    entrada_int = int(entrada)


    par_impar = entrada_int % 2 == 0


    par_impar_texto = 'impar'



    if par_impar:


        par_impar_texto = 'par'



    print(f'o numero {entrada_int} eh {par_impar_texto}')


else:


    print('voce nao digitou um numero inteiro')




    
    





