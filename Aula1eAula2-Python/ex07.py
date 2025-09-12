#Entrar via teclado com o valor de cinco produtos. Após as entradas, digitar um valor referente ao pagamento da somatória destes valores. Calcular e exibir o troco que deverá ser devolvido.

produto1 = float(input("Digite o valor do primeiro produto: "))
produto2 = float(input("Digite o valor do segundo produto: "))
produto3 = float(input("Digite o valor do terceiro produto: "))
produto4 = float(input("Digite o valor do quarto produto: "))
produto5 = float(input("Digite o valor do quinto produto: "))

valor_total = produto1 + produto2 + produto3 + produto4 + produto5

print(f"O valor total do produto ficou em: R$: {valor_total:.2f}")
valor_pagamento = float(input("Qual valor você irá dar ao caixa para finalizar a compra: R$: "))

if (valor_pagamento < valor_total):
  print("Canalha, você não pode realizar a compra!")
elif (valor_pagamento == valor_total):
  print("Sem troco. Obrigado e volte sempre!")
else:
  troco = valor_pagamento - valor_total
  print(f"Seu troco ficou R$: {troco:.2f}. Obrigado e volte sempre!")