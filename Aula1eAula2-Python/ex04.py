#Calcular e exibir a média aritmética de quatro valores quaisquer que serão digitados.

print("Média aritmética de quatro valores: ")

valor1 = float(input("Digite o primeiro valor para calcular a média aritmética: "))
valor2 = float(input("Digite o segundo valor para calcular a média aritmética: "))
valor3 = float(input("Digite o terceiro valor para calcular a média aritmética: "))
valor4 = float(input("Digite o quarto valor para calcular a média aritmética: "))

media = (valor1 + valor2 + valor3 + valor4) / 4

print(f"A média dos valores é: {media}")