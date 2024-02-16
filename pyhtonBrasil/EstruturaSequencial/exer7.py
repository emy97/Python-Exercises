#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado_quadrado = input('Digite a medida do LADO DO QUADRADO: ')
lado_quadrado_float = float(lado_quadrado)

area = lado_quadrado_float * lado_quadrado_float

print(f'A areá é: {area:.2f}')