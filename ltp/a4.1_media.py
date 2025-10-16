n1 = None
n2 = None
invalido = True

while invalido:
    try:
        if n1 == None:
            n1 = float(input("Informe a sua primeira nota: "))
        elif n2 == None:
            n2 = float(input("Informe a sua segunda nota: "))
            invalido = False
        else:
            raise ValueError
    except ValueError:
        print("ERRO: Número inválido!")

media = (n1 + n2) / 2

print(f"Média: {media}")

#n2 = float(input("Informe a sua segunda nota: "))
