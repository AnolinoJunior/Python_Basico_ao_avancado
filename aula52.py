'''
CUidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória ( mutável)
'''
nome = 'Anolino'
emoutra_variavel = nome
nome = 'Alves'
print(nome)
print(emoutra_variavel)