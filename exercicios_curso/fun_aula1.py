"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""
def imprimir(a, b, c):
    print(f'{a}')
    print(f'{b}')
    print(f'{c}')


x = input('Digite: ')
y = input('Digite: ')
z = input('Digite: ')


imprimir(3, 4, 5)# é uma função por padrao
imprimir(x, y, z)

def saudacao(nome = 'Sem nome'):
    print(f'Ola {nome} !')


nome_comp = input('Digiteum nome: ')
saudacao(nome_comp)