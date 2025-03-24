#Manipulando as chaves 
pessoa = {}

##
##

chave = 'nome'

pessoa[chave] = 'Anolino Alves'
pessoa['sobrenome'] = 'Junior'

print(pessoa[chave])

pessoa[chave] = 'Mariana'

del pessoa['sobrenome']
print(pessoa)


if pessoa.get('sobrenome') is None:
    print('Não existe')
else : 
    print (pessoa['sobrenome'])