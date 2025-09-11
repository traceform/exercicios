def calculaDesconto(valor: float, desconto: float) -> float:
    return valor - (valor * desconto / 100)

def calculaJuros(valor, juros):
    return valor * (1 + (juros / 100))
