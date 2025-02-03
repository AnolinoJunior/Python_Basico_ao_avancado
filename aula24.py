'''
interpolaçao basica de strings
s - string
d e i - int
f - float
x e x - hexadecimal (ABCDEF0123456789)
'''
nome = 'Anolino'
preco = 1000.95897643
variavel = '%s, o preço eh R$%.2f' % (nome,preco)
print(variavel)
print('O hexadecimal de %d eh %04x' % (151,151))