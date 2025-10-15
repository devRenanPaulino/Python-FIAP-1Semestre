num = 0
i = 1
soma = 0
pos = 0
neg = 0


while num <= 0 or num > 20:
    num = int(input('Digite a quantidade de números que você deseja entrar via teclado: (1-20)'))

while i <= num:
    valor = int(input(f'Digite o {i}° valor: '))

    if i == 1:
        maior = valor
        menor = valor

    soma += valor
    if (valor > maior):
        maior = valor

    if (valor < menor):
        menor = valor

    if (valor >= 0):
        pos += 1
    else:
        neg = + 1

    i += 1

media = soma / num
per_neg = (neg * 100) / num
per_pos = (pos * 100) / num

print(f"O maior número: {maior}")
print(f"O menor número: {menor}")
print(f"A soma dos números: {soma}")
print(f"A média dos números: {media}")
print(f"O percentual números positivos: {per_pos}")
print(f"O percentual números negativos: {per_neg}")

