#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
while True:
    populacao_a = int(input('Qual é o tamanho da população A? '))
    while populacao_a == 0:
        print('População tem que ser maior que 0 !')
        populacao_a = int(input('Qual é o tamanho da população A? '))


    populacao_b = int(input('Qual o tamanho da população B? '))
    while populacao_b == 0:
        print('População tem que ser maior que 0 !')
        populacao_b = int(input('Qual o tamanho da população B? '))

    taxa_a = float(input('Digite a taxa de crescimento anual da população A: '))
    while taxa_a == 0.0:
        print('Taxa tem que ser maior que 0 ! ')
        taxa_a = float(input('Digite a taxa de crescimento anual da população A: '))

    taxa_b = float(input('Digite a taxa de crescimento anual da população B: '))
    while taxa_b == 0.0:
        print('Taxa tem que ser maior que 0 ! ')
        taxa_b = float(input('Digite a taxa de crescimento anual da população B: '))
    
    anos = 0

    while populacao_a <= populacao_b:
        populacao_a *=(1 + taxa_a)
        populacao_b *=(1 + taxa_b)
        anos += 1

    print(f'Sera necessario {anos} anos para que a população do país A ultrapasse ou iguale a população do país B')

    dnv = input('Deseja continuar [s]sim [n]nao?  ').lower()
    print(dnv)
    while dnv != 's' and dnv != 'n':
        print('Digite s ou n')
        dnv = input('Deseja continuar [s]sim [n]nao?').lower()
    if dnv == 's':
        print('Insira os dados novamente ! ')
        continue
    else:
        print('Encerrou o programa ! ')
        break
