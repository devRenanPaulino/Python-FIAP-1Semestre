num = int(input('Entre com a base a ser multiplicada: '))

while num <= 0:
    print('Valor Inválido')
    num = input("Digite um valor positivo: ")

a = int(input('Digite o valor de partida: (ex: 4)'))
b = int(input('Digite o intervalo onde deve para a multiplicação: (ex: 10)'))

while b <= a:
    print("O intervalo de termino deve ser maior que o valor inicial!")
    b = input('Digite o intervalo onde deve para a multiplicação: (ex: 10)')

for i in range(b, a - 1, -1):
    resultado = num * i
    print(f'{num} * {i} = {resultado}')