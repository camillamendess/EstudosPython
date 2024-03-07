'''a = float(input('Digite o valor do cateto 1: '))
b = float(input('Digite o valor do cateto 2: '))
h = (a ** 2 + b ** 2) ** (1/2)
print('O valor da hipotesuna é {:.2f}'.format(h)'''
import math
co = float(input('o comprimento do cateto op é:  '))
ca = float(input('o comprimento do cateto ad é:  '))
hi = math.hypot(co,ca)
print('O valor da hipotenusa é {:.2f}'.format(hi))

