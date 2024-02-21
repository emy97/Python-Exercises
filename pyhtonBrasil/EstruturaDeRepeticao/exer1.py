#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

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
        
