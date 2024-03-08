from random import  randint
computador = randint(0, 5)
print('-=-' * 20)
print('vou pensar em um número entre 0 e 5. Tente adivinhar...rsrs')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?'))
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer')
else:
    print(('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador)))