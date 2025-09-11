from util import calculaJuros

valor = float(input("Informe o valor do produto: R$"))
juros = float(input("Informe o valor dos juros simples: %"))

print(f"Valor: R${calculaJuros(valor, juros):.2f}")
