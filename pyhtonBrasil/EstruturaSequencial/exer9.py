#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

fahr = input('Digite a temperatura em Fahrenheit (°F):  ')

fahr_float = float(fahr)
conv_cel =5 * ((fahr_float - 32)/9)

print(f'convertido ficou (°C):{conv_cel:.1f}')

