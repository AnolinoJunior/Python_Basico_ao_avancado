'''
iteravel - > str, range, etc (__iter__) metodo (eh o que voce 
chama depois dos = por exemplo: nome = anolino nome.isdigit chamando um metodo)
iterador - > quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter - > me entregue seu iterador
'''

numeros = range (0, 100, 8)

for numero in numeros:
    print(numero)