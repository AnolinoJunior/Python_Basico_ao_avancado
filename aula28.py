'''
introduçao ao try/except
try -> tentar executar o codigo
except -> ocorreu algum erro ao tentar executar
'''
numero_str = input ('Vou Dobrar o numero que voce digitar:')

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} eh  {numero_float * 2:.0f}') 
    # PEGUEI OS DOIS VALORES NOMEADOS TRANSFORMEI E MUTIPLIQUEI
except:
    print('Isso nao eh um numero')
    

'''
if numero_str.isdigit():

    numero_float = float{numero_str}
    print(f'O dobro de {numero_str} eh  {numero_float * 2:.0f}')
 else:
     print('isso nao eh um numero inteiro')
     '''