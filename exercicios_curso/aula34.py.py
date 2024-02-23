'''senha_salva = '1234567'
senha_digitada = ''
i = 0

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({i}x): ')
    i += 1

    if i > 3:
        print('Errou mts vezes')
        break
   '''

texto = 'Pedro te amo'
novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto)
