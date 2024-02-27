#Faça um Programa que peça as quatro notas de 10 alunos, 
#calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

notas = []
medias = []
maior = 0
soma = 0 
qtd_notas = 4

for i in range(10):
    print(f'--Aluno {i + 1}-- ')

    for j in range(qtd_notas):
        nota = float(input(f'Digite sua {j + 1} nota: '))
        notas.append(nota)
        
    soma = sum(notas)
    notas.clear()
    
    media = soma /qtd_notas
    medias.append(media)
    soma = 0

    if medias[i] >= 7:
        maior += 1

print(f'medias da sala : {medias:.2f}')
print(f'apenas {maior} alunos tem notas maior qou igual a 7')