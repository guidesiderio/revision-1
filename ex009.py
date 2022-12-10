print('Produto mais barato:')

produto1 = input('Digite o preço do primeiro produto: ')
produto2 = input('Digite o preço do segundo produto: ')
produto3 = input('Digite o preço do terceiro produto: ')

a = float(produto1)
b = float(produto2)
c = float(produto3)

menor = 0
if a == b and a == c:
    menor = 'A, B ou C'
elif a == b and a < c:
    menor = 'A ou B'
elif a == c and a < b:
    menor = 'A ou C'
elif b == c and b < a:
    menor = 'B ou C'
if a < b and a < c:
    menor = 'A'
elif b < a and b < c:
    menor = 'B'
elif c < a and c < b:
    menor = 'C'

print(f'Você deve comprar o produto: {menor}')
