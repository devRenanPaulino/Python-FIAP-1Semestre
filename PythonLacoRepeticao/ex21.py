num = int(input('Digite um valor positivo para ser multiplicado: '))

while num <= 0:
    print("Digite um valor positivo!")
    num = input('Digite um valor positivo para ser multiplicado:')

menor_intervalo = int(input("Intervalo que o programa deverá começar: (menor valor)"))
maior_intervalo = int(input("Digite o ultimo valor que deverar ser multiplicado: (valor deve ser o maior)"))

while maior_intervalo < menor_intervalo:
    maior_intervalo = input("Digite o ultimo valor que deverar ser multiplicado: (valor deve ser o maior)")

while maior_intervalo >= menor_intervalo:
    resultado = num * maior_intervalo
    print(f'{num} X {maior_intervalo} = {resultado}')
    maior_intervalo -= 1
