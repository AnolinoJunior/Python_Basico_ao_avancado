'''

Constante = "variaveis" que nao vao mudar muitas condiçoes no mesmo if (ruim)

    <- Contagem de complexidade (ruim)
'''

velocidade = 61 # velocidade atual do carro

local_carro = 99 # local em que o carro da na estrada



radar_1 = 60 # velocidade maxima no radar 1 

local_1 = 100 # local onde o radar 1 esta 

radar_range = 1 # a distancia onde o radar pega 

velocidade_carro_passou_radar_1 = velocidade > radar_1
carro_passou_radar_1 = local_carro >= (local_1 - radar_range) and local_carro <= (local_1 + radar_range) and velocidade_carro_passou_radar_1
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1

if velocidade_carro_passou_radar_1:

    print('velocidade carro passou do radar_1')

if carro_passou_radar_1:
    print('carro passou radar_1')    


if carro_multado_radar_1:

    print('voce ultrapassou o limite de radar_1')


