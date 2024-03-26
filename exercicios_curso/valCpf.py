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
"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""


primeiro_digito = 0
segundo_digito = 0

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
    print(f'resultado do primeiro digito é {primeiro_digito}')
    primeiro_digito = 0
else:
    print(f'resultado do primeiro digito é {resto}')
    primeiro_digito = resto


#zerando
calculo = 0
seg_cpf_conta = []
soma_calculo = 0
resto = 0


#Calculo digito 2
contador = 11
for digito in nove_digitos:
    calculo = int(digito) * contador
    seg_cpf_conta.append(calculo)
    contador -= 1

soma_calculo = (sum(cpf_conta)) * 10

resto = soma_calculo % 11
if soma_calculo % 11 > 9:
    segundo_digito = 0
    print(f'resultado do segundo digito é {segundo_digito}')
else:
    segundo_digito = resto
    print(f'resultado do segundo digito é {resto}')


ultimo_dois_digitos = str(primeiro_digito) + str(segundo_digito)
print(ultimo_dois_digitos)

if ultimo_dois_digitos == cpf[-2:]:
    print('CPF Valido')
else:
    print('CPF invalido')
