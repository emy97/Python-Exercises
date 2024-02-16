"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

radar_1_velocidade = velocidade > RADAR_1
radar_1_range_cima = local_carro >= (LOCAL_1 - RADAR_RANGE)
radar_1_range_baixo = local_carro >= (LOCAL_1 - RADAR_RANGE)

if velocidade > RADAR_1:
    print('Carro passou do radar !')


if radar_1_range_cima and \
    radar_1_range_baixo and \
        radar_1_velocidade:
        print('Carro multado em radar 1')