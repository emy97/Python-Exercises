'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''

arquivo = float(input('Digite o tamanho do arquivo em MB : '))
velocidade = float(input('Digite a velocidade [Mbps]: '))

tempo = (arquivo / velocidade) * 8 # conversao em bits
minuto = tempo / 60.0

print(f'A tempo é {minuto:.2f} minutos, em segundos é {tempo:.2f}') 

'''

A abreviação de Megabyte, ou Mega, é MB, enquanto Megabit, ou Mbps, pode ser representado por Mb 
(sempre com “b” minúsculo). 
Ainda assim, essas são unidades diferentes — sendo o “bit” oito vezes menor que o “byte”.

'''