# descobrindo se o numero eh par
entrada = input('Digite um numero inteiro :')
 
if entrada.isdigit():

    entrada_int = int(entrada)

    par_impar = entrada_int % 2 == 0
    
    par_impar_texto = 'Impar'

    if par_impar :
    
        par_impar_texto = 'Par'

        
    print(f'seu numero {entrada_int} eh {par_impar_texto}')


else: 
     print ('voce nao digitou um numero')    
    


  