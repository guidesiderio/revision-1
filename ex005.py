print('Salário no referido mês:')

ganho_hora = input('Digite quanto você ganha por hora: ')

horas_trabalhadas_mes = input('Digite quantas horas você trabalhou por mês: ')

ganho_hora_float = float(ganho_hora)
horas_trabalhadas_mes_float = float(horas_trabalhadas_mes)

salario = ganho_hora_float * horas_trabalhadas_mes_float

print(f'O seu salário é igual a R$ {salario:.2f}')
