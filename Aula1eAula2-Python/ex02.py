import math

lado1 = float(input("Digite o valor do primeiro lado: "))
lado2 = float(input("Digite o valor do segundo lado: "))

if lado1 == lado2:
    print("É um quadrado!")
    area = math.pow(lado1, lado1)
    print(f"E sua área é {area}")
else:
    print("Não é um quadrado. Informe valores correspondentes com um quadrado (lados iguais)")
