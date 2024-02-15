#.......1234567891011
nome = 'Emily Comin' #iteravel

tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[1])

indice = 0
novo_nome = ''

while indice <  len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

print(novo_nome)