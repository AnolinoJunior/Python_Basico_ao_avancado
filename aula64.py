"""
Introdução ás funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um alor específico.
Por padrão, funções Python retornam None (nada).
"""

# def imprimir (a,b,c): 
#   print(a,b,c)

#imprimir(1,2,3) #Argumento (Valor) "Executando a ação"
#imprimir(4,5,6)
#imprimir(7,8,9)
#imprimir(10,11,12)

def saudacao(nome):
    print(f'Olá, {nome}!')


saudacao('Anolino')
saudacao('Mariana')
saudacao('Trabalho')