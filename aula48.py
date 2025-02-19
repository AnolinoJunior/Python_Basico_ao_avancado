"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
produto_higiene = 'Shampoo, Detergente, Pasta de dente, Alcool em gel, Agua sanitaria, Papel higenico'
porcarias = 'Chocolate, M&M, Amendoin, Doritos, Ovo de pascoa '
lista = ['Mercado', [produto_higiene],'Americanas', [porcarias]]
print(lista)
print(lista[3])
