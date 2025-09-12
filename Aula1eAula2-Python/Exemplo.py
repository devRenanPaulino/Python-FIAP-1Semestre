print("Hello, World!")

nome = str(input("Digite o nome do aluno: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
print("A média é:", media)

if media <= 6:
    print("Reprovado")
else:
    print("Aprovado")

