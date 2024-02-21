#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.


'''

TENTATIVA 1 

while True:
    try:
        nota = int(input('Digite uma nota entre 0 e 10: '))

    except:
        print('Erro, digite um valor valido ! ')
        continue

    if nota > 10:
        print('Digite entre 0 e 10 !!')
        continue
    elif nota < 0:
        print('Digite entre 0 e 10 !!')
        continue
    else:
        print(f'Nota digitada {nota} ! ')
        break
        

'''
#Estudei mais um  pouco e vi como diminuir o codigo ~ TENTATIVA 2

nota = int(input('Digite uma nota de 0 a 10: '))

while nota > 10 or nota < 0:
    print('digite um valor entre 0 a 10! ')
    nota = int(input('Digite uma nota de 0 a 10: '))

print(' Saiu do while, fim do programa ')