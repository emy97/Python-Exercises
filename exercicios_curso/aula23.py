"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'

print(variavel[4:])#fatiamento
print(variavel[4:6])
print(variavel[:4])

print(len(variavel))

print(reversed(variavel))