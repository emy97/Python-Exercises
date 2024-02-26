#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

vetor = []
consoante = 0
vogal = 0

for i in range(10):
    letra = input(f'Digite a {i + 1} letra: ').lower()
    vetor.append(letra)
    
    if letra.isalpha():  # Verifica se é uma letra
        if letra not in 'aeiou':
            consoante += 1
        else:
            vogal += 1
print(f'Total vogais {vogal}, total consoantes {consoante}')
    


