from math import sqrt
x1 = int(input("Digite o valor de x do ponto 1: "))
y1 = int(input("Digite o valor de y do ponto 1: "))
x2 = int(input("Digite o valor de x do ponto 2: "))
y2 = int(input("Digite o valor de y do ponto 2: "))
distancia = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
if distancia >= 10:
    print("longe")
else:
    print("perto")
