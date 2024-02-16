#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = input('Qual o RAIO do circulo: ')
raio_float = float(raio)

PI = 3.14

area = PI * (raio_float * raio_float)

print(f'A area é : {area:.2f}')