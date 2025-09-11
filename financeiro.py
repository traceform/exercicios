from util import calculaDesconto

valor = float(input("Informe o valor do produto: "))
desconto = float(input("Informe o desconto: %"))

print(f"Valor com desconto: R${calculaDesconto(valor, desconto):.2f}")