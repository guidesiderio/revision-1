print('Cálculo da Média Bimestral:')
nota1 = input('Digite a primeira nota: ')
nota2 = input('Digite a segunda nota: ')
nota3 = input('Digite a terceira nota: ')
nota4 = input('Digite a quarta nota: ')

nota1_float = float(nota1)
nota2_float = float(nota2)
nota3_float = float(nota3)
nota4_float = float(nota4)

media = (nota1_float + nota2_float + nota3_float + nota4_float) / 4

print(f'Média = {media:.2f}')
