import math
ângulo = float(input('Digite o ângulo que você deseja!: ' ))
s = math.sin(math.radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'. format(ângulo, s))
c= math.cos(math.radians(ângulo))
print('O ângulo de {}tem o COSSENO de {:.2f}'.format(ângulo,c))
t = math.tan(math.radians(ângulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo,t))




