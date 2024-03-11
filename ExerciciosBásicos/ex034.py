print('( ͡° ͜ʖ ͡°)'*2)
print('analisador de Triângulos')
print('( ͡° ͜ʖ ͡°)'*2)
r1 = float(input('primeiro segmento: '))
r2 = float(input('primeiro segmento: '))
r3 = float(input("Terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('O segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo!')
