print('Maior número:')

valor1 = input('Digite o primeiro valor: ')
valor2 = input('Digite o segundo valor: ')
valor3 = input('Digite o terceiro valor: ')

a = float(valor1)
b = float(valor2)
c = float(valor3)

maior = 0
if a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b
else:
    maior = c

print(f'O maior valor é: {maior}')
