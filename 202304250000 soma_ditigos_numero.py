num = int(input("Digite um número inteiro: "))
soma = 0
while num > 0:
    digito = num % 10
    soma = soma + digito
    num = num // 10
print(soma)
