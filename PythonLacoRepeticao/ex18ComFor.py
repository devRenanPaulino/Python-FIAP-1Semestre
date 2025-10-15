num = int(input('Digite um valor para eu te apresentar a tabuada respectiva: '))

while num <= 0:
    print('O valor deve ser positivo!')
    num = input('Digite um valor para eu te apresentar a tabuada respectiva: ')

for i in range(1,11,1):
    resultado = num * i
    print(f'{num} X {i} = {resultado}')
