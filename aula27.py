'''
Exercicio
Peça ao usuario para digitar seu nome
Peça ao usuario para digitar sua idade
Se nome e idade forem digitados :
    Exiba:
            Seu nome e {nome}
            Seu nome invertido e {nome invertido}
            Se nome contem (ou nao espaços)
            Seu nome tem {n} letras
            A primeira letra do seu nome eh {letra}
            A ultima letra do seu nome eh {letra}
Se nada for digitado em nome ou idade: 
    Exiba "Desculpe, voce deixou os campos vazios."
    '''

nome = input ("Digite seu nome:")
idade = input ("Digite sua idade:")

if nome and idade:
    print(f'Seu nome eh {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome :
        print('Seu nome contem espaços')
    else :
        print('Seu nome nao contem espaços')
    
        print(f'Seu nome tem {len(nome)} letras')
        print(f'A primeira letra do seu nome eh {nome[0:1]}')
        print(f'A ultima letra do seu nome eh {nome[-1:]}')
else :
        print('Desculpe,voce deixou os campos vazios')    
