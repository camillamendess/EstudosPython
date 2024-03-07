numero = int(input('Digite um numero para ver sua tabuada: '))
numero2 = 0
print('_'*20)
print('{} x {:2} = {}'.format(numero, 1, (numero*1)))
print('{} x {:2} = {}'.format(numero, 2,  (numero*2)))
print('{} x {:2} = {}'.format(numero, 3, (numero*3)))
print('{} x {:2} = {}'.format(numero, 4, (numero*4)))
print('{} x {:2} = {}'.format(numero, 5, (numero*5)))
print('{} x {:2} = {}'.format(numero, 6, (numero*6)))
print('{} x {:2} = {}'.format(numero, 7, (numero*7)))
print('{} x {:2} = {}'.format(numero, 8, (numero*8)))
print('{} x {:2} = {}'.format(numero, 9, (numero*9)))
print('{} x {:2} = {}'.format(numero, 10, (numero*10)))
print('_'*20)

# Outra maneira de fazer, com o for
numero = int(input('Digite um número para ver sua tabuada: '))

print('_'*20)
for i in range(1, 11):
    print('{} x {:2} = {}'.format(numero, i, (numero*i)))
print('_'*20)
