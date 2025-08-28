def convertDolarReal(valor, cotacao):
    return valor/cotacao

print(f"R${convertDolarReal(100, 0.18):.2f}")