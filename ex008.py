print('Maior e menor:')

valor1 = input('Digite o primeiro valor: ')
valor2 = input('Digite o segundo valor: ')
valor3 = input('Digite o terceiro valor: ')

a = float(valor1)
b = float(valor2)
c = float(valor3)

maior = 0
menor = 0
if a >= b and a >= c:
    maior = a
    if b > c:
        menor = c
    else:
        menor = b
elif b >= a and b >= c:
    maior = b
    if a > c:
        menor = c
    else:
        menor = a
elif c >= a and c >= b:
    maior = c
    if a > b:
        menor = b
    else:
        menor = a

print(f'Maior = {maior}, Menor = {menor}')
