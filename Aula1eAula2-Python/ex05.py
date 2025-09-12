# Entrar via teclado com o valor de uma temperatura em graus Celsius, calcular e exibir sua temperatura equivalente em Fahrenheit.
print("Conversão de Celsius para Fahrenheit: ")

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = celsius * 9 / 5 + 32

print(f"{celsius}°C = {fahrenheit}°F")