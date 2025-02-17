'''
Repetições
while (equanto)
Executa uma ação equanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
'''
condicao = True

while condicao :
    nome = input ('Qual o seu nome? :')
    print(f'Seu nome é {nome}')

    if nome == 'sair' :
        break

print('Encerrado')        
