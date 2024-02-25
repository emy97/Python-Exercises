#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []
soma = 0.0

for i in range(1, 5):
    nota = float(input(f'Insira sua {i}ª nota: '))
    notas.append(nota)
    soma += nota

media = soma / 4
print("Notas:", notas)
print("Média:", media)
