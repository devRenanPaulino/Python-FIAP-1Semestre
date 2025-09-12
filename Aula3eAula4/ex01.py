print("Média do Aluno")

p1 = float(input("Digite a primeira nota da p1: "))
p2 = float(input("Digite a segunda nota da p2: "))

m = (p1 + p2) / 2

if (m >= 5):
    print("Aprovado!")
else:
    print("Reprovado!")

print(f"A sua nota foi: {m}")

print("Fim Programa!")