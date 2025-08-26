#Exercícios que fiz em https://panda.ime.usp.br/cc110/static/cc110/05-if.html

#Exercício 1
cont, soma = 1, 0
while cont < 8:
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        soma = soma + num
    cont = cont + 1
print(soma)

#Exercício 2
cont, n, pares, impares = 0, int(input("Tamanho da sequência: ")), 0, 0
while cont < n:
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    cont = cont + 1
print(f"Total na sequência de {n} números:\nPares: {pares}\nÍmpares: {impares}")

#Exercício 3
novoNumAlvo = numAlvo = int(input("Digite um número inteiro maior que zero: "))
numBusca = int(input("Digite um número entre 0 e 9 que quer buscar no anterior: "))
cont = totalVezes = 0
while cont < len(str(numAlvo)):
    if novoNumAlvo % 10 == numBusca:
        totalVezes = totalVezes + 1
    novoNumAlvo = novoNumAlvo // 10
    cont = cont + 1
print(f"O dígito {numBusca} aparece {totalVezes} vezes em {numAlvo}.")