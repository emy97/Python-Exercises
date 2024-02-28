#Faça um Programa que peça a idade e a altura de 5 pessoas, 
#armazene cada informação no seu respectivo vetor. Imprima a idade e a 
#altura na ordem inversa a ordem lida.

idades = []
alturas = []

for i in range(3):
    print(f'Pessoa {i+1} Preencha os baixos a baixo : ')
    altura = float(input(f'Digite sua altura : '))
    alturas.append(altura)
    idade = int(input(f'Digite sua idade: '))
    idades.append(idade)

idades.reverse()
alturas.reverse()
print(f'Idades:{idades}')
print(f'Alturas: {alturas}')

...