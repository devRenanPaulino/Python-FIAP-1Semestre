print("Calculadora de peso ideal")

altura = int(input("Digite sua altura em metros: "))
peso = float(input("Digite o seu peso: "))

imc = peso / (altura * altura)

if (imc < 20):
    print("Abaixo do peso")
elif (imc < 25):
    print("Peso Ideal!")
else:
    print("Acima do Peso!")


print("Fim Programa!")
