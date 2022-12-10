print('Ordem decrescente:')

valor1 = input('Digite o primeiro valor: ')
valor2 = input('Digite o segundo valor: ')
valor3 = input('Digite o terceiro valor: ')

a = float(valor1)
b = float(valor2)
c = float(valor3)

maior = 0
medio = 0
menor = 0
if a >= b and a >= c:
    maior = a
    if b > c:
        medio = b
        menor = c
    else:
        medio = c
        menor = b
elif b >= a and b >= c:
    maior = b
    if a > c:
        medio = a
        menor = c
    else:
        medio = c
        menor = a
elif c >= a and c >= b:
    maior = c
    if a > b:
        medio = a
        menor = b
    else:
        medio = b
        menor = a

print(f'{maior} < {medio} < {menor}')
