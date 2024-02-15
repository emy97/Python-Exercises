"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

#RESOLUÇÃO

num = input('Digite um numero inteiro: ')

try:
    num_int = int(num)
    resto = num_int % 2
    
    if resto == 0:
        print('o numero digitado é PAR')
    else:
        print('o numero digitado é IMPAR')

except: 
    print('Erro no conteudo digitado')

"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.


# RESOLUÇÃO

hora = input('Digite a hora atual, apenas a hora 00 as 23: ')

try:
    hora_int = int(hora)

    bom_dia = hora_int >= 0 and hora_int <= 11
    boa_tarde = hora_int >= 12 and hora_int <= 17
    boa_noite = hora_int >= 18 and hora_int <= 23

    if bom_dia:
        print('Bom dia')
    elif boa_tarde:
        print('Boa tarde')
    elif boa_noite:
        print('Boa noite')
    else:
        print('Numero digitado esta fora do 00 a 23')
except:
    print('Digite um numero')
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

#RESOLUÇÃO

nome = input('Digite seu primeiro nome: ')
nome_cont = len(nome)

if nome_cont >= 0 and  nome_cont <= 4:
    print('Seu nome é curto')
elif nome_cont >= 5 and nome_cont <= 6:
    print('Seu nome é de tamanho normal')
else:
    print('Seu nome é muito grande')
"""

