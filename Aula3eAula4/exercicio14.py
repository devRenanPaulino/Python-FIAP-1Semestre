peso = float(input("Digite o seu peso: "))
altura = float(input("Digite o sua altura: "))

imc = peso / (altura * altura)

if (imc < 20):
  print("Abaixo do peso.")
elif (imc < 25):
  print("Peso Ideal.")
else:
  print("Acima do peso.")