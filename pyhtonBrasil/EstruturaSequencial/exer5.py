#Faça um Programa que converta metros para centímetros.

metros = input('Digite quantos metro sera convertido para centimetros: ')
metros_float = float(metros)

cent = (metros_float) * 100

print(f'a conversao deu: {cent:.2f} centimetros')