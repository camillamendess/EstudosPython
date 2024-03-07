dia = int(input("quantos dias alugado? "))
km = float(input('quantos km foram percorridos? '))
valorDiario = dia * 60
valorrodado = km * 0.15
print('o valor a pagar é R${}'.format(valorDiario + valorrodado))
