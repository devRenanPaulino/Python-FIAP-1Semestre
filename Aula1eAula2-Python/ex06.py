#Entrar via teclado com o valor da cotação do dólar e uma certa quantidade de dólares. Calcular e exibir o valor correspondente em Reais (R$)

print("Conversor de Dólar para Reais")
dolar = float(input("Digite a quantia em dolares: "))

reais = dolar * 5.45

print(f"USD: {dolar:.2f} = R$: {reais:.2f}")