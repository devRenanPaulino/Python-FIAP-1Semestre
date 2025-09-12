base = float(input("Digite a base do terreno: "))
altura = float(input("Digite a altura do terreno: "))

area = base * altura

if (area > 100):
  print("Terreno Grande")
else: 
  print("Terreno Pequeno")