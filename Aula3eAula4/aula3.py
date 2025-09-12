idade = int(input("Digite sua idade: "))

if (idade >= 18):
    print("Carro")
elif (idade < 18 and idade > 0):
    print("Bike")
else:
    print("Digite um valor válido")

print("Fim programa!")