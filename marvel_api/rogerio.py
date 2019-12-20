from math import sqrt

print('============================')
print('     EQUAÇÃO DE 2° GRAU     ')
print('============================')

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))
delta = (b)**2 - 4*(a)*(c)
x_positivo = 0
x_negativo = 0

print(f'\nΔ = ({b}²) - 4 . ({a}) . ({c})')
print(f'Δ = {b**2} - 4 . {a*c}')
print(f'Δ = {b**2} {-4*a*c}')
print(f'Δ = {delta}\n')

if delta == 0:

    if b < 0 and a < 0:
        x_zero = (b*-1) / (2 * (a*-1))
        print(f'x = (-({b})) / 2 . (-{a})')
        print(f'x = {x_zero}')

    elif b < 0:
        x_zero = (b*-1) / (2 * (a))
        print(f'x = (-({b})) / 2 . {a}')
        print(f'x = {x_zero}')

    elif a < 0:
        x_zero = (b) / (2 * (a*-1))
        print(f'x = ({b}) / 2 . (-{a})')
        print(f'x = {x_zero}')

    else:
        x_zero = (b) / (2 * (a))
        print(f'x = ({b}) / 2 . ({a})')
        print(f'x = {x_zero}')


elif delta > 0:

    if b < 0 and a < 0:
        x_positivo = ((b * -1) + sqrt(delta)) / (2 * (a * -1))
        x_negativo = ((b * -1) - sqrt(delta)) / (2 * (a * -1))

        print('---ACHANDO O X COM OPERAÇÃO DE SOMA---\n')
        print(f'x = (-({b})) + √{delta} / 2 . (-{a})')
        print(f'x = {x_positivo}')

        print('---ACHANDO O X COM OPERAÇÃO DE SUBTRAÇÃO---\n')
        print(f'x = (-({b})) - √{delta} / 2 . (-{a})')
        print(f'x = {x_negativo}')


    elif b < 0:
        x_positivo = ((b * -1) + sqrt(delta)) / (2 * (a))
        x_negativo = ((b * -1) - sqrt(delta)) / (2 * (a))

        print('---ACHANDO O X COM O0PERAÇÃO DE SOMA---\n')
        print(f'x = (-({b})) + √{delta} / 2 . {a}')
        print(f'x = {x_positivo}')

        print('---ACHANDO O X COM OPERAÇÃO DE SUBTRAÇÃO---\n')
        print(f'x = (-({b})) - √{delta} / 2 . (-{a})')
        print(f'x = {x_negativo}')

    elif a < 0:
        x_positivo = ((b) + sqrt(delta)) / (2 * (a))
        x_negativo = ((b) - sqrt(delta)) / (2 * (a))

        print('---ACHANDO O X COM OPERAÇÃO DE SOMA---\n')
        print(f'x = (-({b})) + √{delta} / 2 . (-{a})')
        print(f'x = {x_positivo}')

        print('---ACHANDO O X COM OPERAÇÃO DE SUBTRAÇÃO---\n')
        print(f'x = (-({b})) - √{delta} / 2 . (-{a})')
        print(f'x = {x_negativo}')

    else:
        x_positivo = ((b) + sqrt(delta)) / (2 * (a))
        x_negativo = ((b) - sqrt(delta)) / (2 * (a))

        print('---ACHANDO O X COM OPERAÇÃO DE SOMA---\n')
        print(f'x = (-({b})) + √{delta} / 2 . (-{a})')
        print(f'x = {x_positivo}')

        print('---ACHANDO O X COM OPERAÇÃO DE SUBTRAÇÃO---\n')
        print(f'x = (-({b})) - √{delta} / 2 . (-{a})')
        print(f'x = {x_negativo}')

    print(f'x = ({x_positivo}, {x_negativo})')

