#Operadores in e not in 
#Strings são iteráveis
# 0 1 2 3 4 5 6
# A N O L i N o
# -6 -5 -4 -3 -2 -1
'''
nome = 'Anolino'
print(nome[2])
print(nome[0])
print('A' in nome)
print('lino' in nome)
print(10 * '-')
print('Ano' not in nome)
print('zero'not in nome)'''

nome = input ('Digite seu nome:')
encontrar = input ('Digite o que deseja encontrar:')

if encontrar in nome :
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} nao esta em {nome}')