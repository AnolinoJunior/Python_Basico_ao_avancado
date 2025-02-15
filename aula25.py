'''
Formataçao basica de strings
s - string
d - int 
f - float 
. <numero de digitos>f
x ou X - Hexadecimal
(Caractere) (><^) (quantidade)
> - Esquerda
< - Direita
^ - Centro 
Sinal - + ou -
= - Força o numero a aparecer antes dos zeros
Ex. : 0 >- 100, .1f
Conversion flags - !r !s !a
'''
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 eh {1500:08x}')
print(f'{variavel!r}')