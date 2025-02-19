'''
Faça um jogo para o usuário adivinnha qual a palvra secreta.
- Você vai propor uma palavra secreta qualquer e 
vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta
    exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
    Faça a contagem de tentativas do seu usuário.
    '''
  #                01234567  
palavra_secreta = 'programa'
#                 0-1-2-3-4-5-6-7
repeticoes = 0
letras_acertadas = '' 

while True :
    
    letra_digitada = input ('Digite Uma Letra: ')

    repeticoes += 1

    if len(letra_digitada) > 1 :
        print ('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
           palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(palavra_formada)

    if palavra_formada == palavra_secreta :
            print('Voce conseguiu!!!!')
            print(' A Palavra Era', palavra_secreta)
            print(f'Acerto em : {repeticoes} tentativas')
            break

   
    
  
    
    
    
    









