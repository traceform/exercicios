num = int(input("Digite quantos pares você deseja: "))
cont, pares = 1,0
while cont >= 0  and not pares == num:
    if cont % 2 == 0:
        pares = pares + 1
        print(cont)
    cont = cont + 1
