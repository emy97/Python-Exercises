#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = input('Digite a PRIMEIRA nora: ')
nota2 = input('Digite a SEGUNDA nota: ')
nota3 = input('Digite a TERCEIRA nota: ')
nota4 = input('Digite a QUARTA nota: ')

nota1_int = int(nota1)
nota2_int = int(nota2)
nota3_int = int(nota3)
nota4_int = int(nota4)

media = (nota1_int + nota2_int + nota3_int + nota4_int)/4

print(f'A média é: {media}')