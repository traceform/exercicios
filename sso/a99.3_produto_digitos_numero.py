num = int(input("Digite um número inteiro: "))
cont = digito = produto = 1
while num != 0:
    digito = num % 10
    produto = produto * digito
    num = num // 10
print(produto)
