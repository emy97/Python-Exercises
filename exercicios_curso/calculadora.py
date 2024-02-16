#Calculadora com while

resultado = 0

while True:
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Digite o operador desejada: [+]adição [-] subtração [/]Divisão [*]Multiplicação : ')

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        num_validos = True


#ERROS
        
    except Exception as error:
        num_validos = None

    if num_validos is None:
        print('Um dos Numeros estão errados')
        continue

    operador_permitidos = '+-/*'
    if operador not in operador_permitidos:
        print('operador invalido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador. ')
        continue

### OPERAÇÕES
    if operador == '+':
        resultado = num1_float + num2_float
        print(f'A soma deu:{resultado:.2f} ')
     
    elif operador == '-':
        resultado = num1_float - num2_float
        print(f'A subtração deu: {resultado:.2f}')

    elif operador == '/':
        resultado = num1_float / num2_float
        print(f'A divisão deu: {resultado:.2f}')

    elif operador == '*':
        resultado = num1_float * num2_float
        print(f'A multiplicação deu: {resultado:.2f}')


    sair = input('Quer sair? [s]im [n]ão: ').lower()

    if sair == 's' or sair == 'S':
        print('Obrigado por utilizar nossa calculadora')
        break
  

#SAIR
 