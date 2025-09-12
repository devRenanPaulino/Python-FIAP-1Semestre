print("Calculadora de distância e combustível gasto por viagem")

horas = float(input("Digite o tempo da viagem em horas: "))
velocidade_media = float(input("Digite a velocidade média: "))

distancia = velocidade_media * horas
combustivel_gasto = distancia / 12

print(f"A distância percorrida foi: {distancia} km e o combustível gasto foi {combustivel_gasto:.2f} L")
