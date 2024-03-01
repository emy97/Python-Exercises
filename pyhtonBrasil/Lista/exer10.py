#Faça um Programa que leia dois vetores com 10 elementos cada. 
#Gere um terceiro vetor de 20 elementos, cujos valores deverão ser 
#compostos pelos elementos intercalados dos dois outros vetores.

vetor_a = []
vetor_b = []
vetor_c = []
i = 0
j = 0

while i < 10:
    num = int(input(f'Digite 10 numeros inteiros, numero [{i + 1}]: '))
    vetor_a.append(num)
    i+=1

while j < 10:
    num = int(input(f'Digite mais 10 numeros inteiros, numero [{j + 1}]: '))
    vetor_b.append(num)
    j+=1

for a , b in zip(vetor_a, vetor_b):
    vetor_c.append(a)
    vetor_c.append(b)

print(vetor_c)