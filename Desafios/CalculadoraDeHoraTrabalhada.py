# calculadora de salario
print('Calculadora de hora')


while True:
  saida = ''
  total_minutos = 0
  total_ganhado = 0.0
  valor_por_minuto = 0.0
  hr_trabalhada = input('Digite o valor da  sua hora, como no exemplo (12.50): ')
  qtd_hr_trabalhada = input('Digite apenas as horas trabalhadas :')
  qtd_minutos_trabalhados = input('Digite os minutos trabalhados, caso nao tiver, digite 0 :')


  try:
    hr_trabalhada_int = float(hr_trabalhada)
    qtd_hr_trabalhada_int = int(qtd_hr_trabalhada)
    qtd_minutos_trabalhados_int = int(qtd_minutos_trabalhados)
  except:
    print('Error de inserçao, o aplicativo vai encerrar')
    break
    
  if qtd_minutos_trabalhados_int >= 0 and qtd_minutos_trabalhados_int <= 60:
    total_minutos = (qtd_hr_trabalhada_int * 60) + qtd_minutos_trabalhados_int
    valor_por_minuto = hr_trabalhada_int / 60
    total_ganhado = total_minutos * valor_por_minuto
    print(f'O salario ganho do dia e: {total_ganhado:.2f}R$')
    saida = input('Deseja fazer outro calculo? Digite a primeira letra [s]im [n]ao : ?')
    if saida == 'n':
        print('Ate mais')
        break
    else:
        continue