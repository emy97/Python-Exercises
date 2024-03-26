"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""



primeiro_digito = 0

print('Validador de CPF')
while True:
    cpf = input('Digite seu CPF: ')
    cpf = cpf.replace('.', '') # estudar regEx para ser mais eficiente
    cpf = cpf.replace('-', '')
    if len(cpf) < 11 or len(cpf) > 11:
        print('Digite um valor valido')
        continue
    else:
        break

#calculo
nove_digitos = cpf[:9]
contador = 10
cpf_conta = []
for digito in nove_digitos:
    calculo = int(digito) * contador
    cpf_conta.append(calculo)
    contador -= 1
    
print(cpf_conta)

soma_calculo = sum(cpf_conta)
print(soma_calculo)

mult_calculo = soma_calculo * 10

resto = mult_calculo % 11

if resto > 9 :
    print('resultado é 0')
    primeiro_digito = 0
else:
    print(f'resultado é {resto}')
    primeiro_digito = resto