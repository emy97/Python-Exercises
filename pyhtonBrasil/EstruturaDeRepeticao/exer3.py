'''

Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';

'''
'''
TENTATIVA 1

while True:
    try:
        nome = input('Digite seu nome: ')
        idade = int(input('Digite sua idade: '))
        salario = float(input('Digite seu salario: R$ '))
        sexo = input('Digite seu Sexo  [f-feminino] ou [m - masculino]: ').lower()
        estado_civil = input('Digite seu estado civil [s - solteiro], [c - casado], [v - viuvo] ou [d - divorciado]: ').lower()

    except:
        print('Digite valores validos !!')
        continue
    if len(nome) < 3:
        print('Digite um nome maior que 3 caracteres !')
        continue

    elif idade < 0 and idade > 150:
        print('Digite uma idade entre 0 a 150 !')
        continue

    elif salario < 0.0:
        print('Digite um salario maior que 0 ')
        continue

    elif sexo != 'f' and sexo != 'm':
        print('Digite sexo valido, f ou m !! ')
        continue
    elif estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd' :
        print('Digite sexo valido,[s - solteiro], [c - casado], [v - viuvo] ou [d - divorciado]!! ')
        continue

    else:
        print('Tudo certo')
        break
'''
# TENTATIVA 2

print('CADASTRO DE DADOS')
nome = input('Digite seu nome: ')
while len(nome) <= 3:
    print('Digite um nome com mais de 3 caracteres ! ')
    nome = input('Digite seu nome: ')

idade = int(input('Digite sua idade: '))
while idade < 0 or idade > 150:
    print('Digite uma idade entre 0 a 150 ! ')
    idade = int(input('Digite sua idade: '))

salario = float(input('Digite seu salario: R$ '))
while salario == 0:
    print('Digite um salario, não pode ser 0 !')
    salario = float(input('Digite seu salario: R$ '))

sexo = input('Digite um sexo, f - feminino, m - masculino : ').lower()
while sexo != 'f' and sexo != 'm':
    print('Digite um sexo valido ! ')
    sexo = input('Digite um sexo, f - feminino, m - masculino : ').lower()

estado_civil = input('Digite seu estado civil [s - solteiro], [c - casado], [v - viuvo] ou [d - divorciado]: ').lower()
while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    print('Digite um estado civil valido ! ')
    estado_civil = input('Digite seu estado civil [s - solteiro], [c - casado], [v - viuvo] ou [d - divorciado]: ').lower()

print('Dados cadastrados com sucesso !')
     
