'''
Faça um programa que pergunte a hora ao usuario e, baseando-se no horario
descrito, exiba  a saudaçao apropriada, ex
bom dia 0-11, boa 12-17 e boa noite 18-23.
'''
entrada = input ('Digite as horas com numeros inteiros')
try:

     hora = int(entrada)

     if hora >= 0 and hora <= 11 :
        
        print('bom dia ')

     elif >= 12 and hora <= 17 :

        print('boa tarde meu amigo')

     elif >= 18 and hora <= 23 : 
    print('boa noite meu amigo ')

    else:
        print('nao conheco essa hora')
except:
      print('digite numeros inteiros')