v1 = float(input("Digite o primeiro valor distinto: "))
v2 = float(input("Digite o segundo valor distinto: "))
v3 = float(input("Digite o terceiro valor distinto: "))

if (v1 > v2 and v1 > v3):
  print(f"Maior valor: {v1}")
elif (v2 > v1 and v2 > v3):
  print(f"Maior Valor: {v2}")
else:
  print(f"Maior valor: {v3}")
