'''i = 1
while(i<=10):
    print(i)
    i+=1'''

for i in range (1, 11, 1):
    print(i)

num = int(input("Digite um valor para te mostrar a tabuada: "))

while (num <= 0):
    print('Não pode valor negativo!')
    num = int(input("Digite outro valor para obter a tabuada: "))

for i in range(1, 11, 1):
    r = num * i
    print(f"{num} X {i} = {r}")