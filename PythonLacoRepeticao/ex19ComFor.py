soma = 0
pos = 0
neg = 0

for i in range(1, 6, 1):
    num = int(input(f'Entre com o {i}° valor: '))

    if i == 1:
        maior = num
        menor = num

    soma += num

    if num > maior:
        maior = num

    if num < menor:
        menor = num

    if num >= 0:
        pos += 1
    else:
        neg += 1

media = soma / 5
per_neg = (neg * 100) / 5
per_pos = (pos * 100) / 5

print(f"O maior número: {maior}")
print(f"O menor número: {menor}")
print(f"A soma dos números: {soma}")
print(f"A média dos números: {media}")
print(f"O percentual números positivos: {per_pos}")
print(f"O percentual números negativos: {per_neg}")



