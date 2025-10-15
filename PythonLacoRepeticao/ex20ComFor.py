qtde = int(input("Digite a quantidade de números que você quer digitar entre 1 e 20: "))

while qtde <= 0 or qtde > 20:
    print("Valor menor que zero ou maior do que 20")
    qtde = input("Digite a quantidade de números que você quer digitar entre 1 e 20: ")

soma = 0
pos = 0
neg = 0

for i in range(0, qtde, 1):
    num = int(input(f'Digite o {i}° valor: '))

    if i == 0:
        maior = num
        menor = num

    soma += num

    if num > maior:
        maior = num

    if num < menor:
        menor = num

    if num >= 0:
        pos = num
    else:
        neg = num

media = soma / qtde
per_neg = (neg * 100) / qtde
per_pos = (pos * 100) / qtde

print(f"O maior número: {maior}")
print(f"O menor número: {menor}")
print(f"A soma dos números: {soma}")
print(f"A média dos números: {media}")
print(f"O percentual números positivos: {per_pos}")
print(f"O percentual números negativos: {per_neg}")
