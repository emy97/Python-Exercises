#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

'''
while True:
    nome = input('Digite o usuario: ')
    senha = input('Digite a senha: ')

    if nome == senha:
        print('Nome de usuario e senha são as mesmas, digite um valor diferente para ambos !!')
        continue
    elif nome.strip() == '' or senha.strip() == '':
        print('Nome de usuário ou senha não podem ser vazios. Tente novamente.')
        continue
    else:
        print('Tudo certo !! ')
        break

'''
print('Cadastro de usuario')
nome = input('Digite um nome de usuario: ')
senha = input('Digite uma senha: ')

while nome == senha:
    print('Nome de usuario e senha são as mesma, digite diferentes !! ')
    nome = input('Digite um nome de usuario: ')
    senha = input('Digite uma senha: ')

print('Cadastrado com sucesso')   