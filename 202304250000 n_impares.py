n = int(input("Digite o valor de n (total de ímpares): "))
cont = impares = 0
while cont >= 0 and not impares == n:
    if cont % 2 != 0:
        impares = impares + 1
        print(cont)
    cont = cont + 1
