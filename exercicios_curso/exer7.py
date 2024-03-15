print('LISTA DE COMPRAS TOP')

lista = []
while True:
    print('Selecione uma opção')
    opcao = input('\t [i]INSERIR   [a]APAGAR  [l]LISTAR ----> ').lower()
    
    if opcao == 'a' :
        try:
            indice = int(input('Qual indice quer remover ? :'))
            lista.pop(indice)
        except:
            print('Indice digitado não existe')
            continue

    if opcao == 'i':
        try:
            inserir = input('Digite o que vai ser adicionado na lista: ')
            lista.append(inserir)
        except:
            print('Digite um valor valido ! ')
            continue

    if opcao == 'l':
        for i in enumerate(lista):
            print(f'{i}')


            
    continue
