#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# ((°C × 9)/5) + 32 = 32 °F

cel = input('Digite a temperatura em graus Celsius (°C): ')
cel_float = float(cel)

conv = ((cel_float * 9)/5) + 32

print(f'A conversao para Fahrenheit (°F):{conv:.1f} ')