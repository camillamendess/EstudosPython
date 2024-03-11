salario = float(input('Digite o salário: '))
if salario <= 1250.00:
    aumento = salario * 0.15
    print('O salário é {} e com aumento fica {}'.format(salario, (salario + aumento)))
else:
    aumento = salario * 0.1
    print('O salario é {} e com aumento fica {}'.format(salario, (salario + aumento)))