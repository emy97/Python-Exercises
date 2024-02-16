#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input('Digite sua altura: '))

calculo = (altura * 72.7) - 58

print(f'Seu peso ideal é: {calculo:.2f}Kg')