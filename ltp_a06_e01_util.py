def calculaDesconto(valor: float, desconto: int) -> float:
    """Retorna um valor flutuante de um produto com o desconto já aplicado"""
    return valor - (valor * desconto / 100)

def calculaJuros(valor: float, juros: int) -> float:
    """Retorna o valor flutuante de um item com os juros simples já aplicados"""
    return valor * (1 + (juros / 100))


