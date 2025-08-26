'''Escreva um programa que receba um número inteiro positivo na entrada e
verifique se é primo. Se o número for primo, imprima "primo". Caso contrário,
imprima "não primo".'''

from math import sqrt
num = int(input("Digite um número inteiro: "))
cont = divisivel = 2
k = 0
while cont < num:
    k = num / cont
#if k == int(k) or num == 3 and num % num == 0: #o resto da divisão de 9 por 3 não pode ser 0, caso contrátio não é primo
    if num % 2 == 0 and num == 2 or num % 3 == 0 and num == 3 or k != int(k):
        divisivel = True
    else:
        divisivel = False
    print(f"cont: {cont}, divisivel {divisivel}")
    cont = cont + 1
if divisivel:
    print("não primo")
else:
    print("primo")
    






'''
nao divisivel por 2 nem por 3
cont = 1
resultado = 'nenhum'
while cont <= 100:
    if num // cont != cont and num % cont != 0 and sqrt(num) != cont ** 2:
        resultado = True
    else:
        resultado = False
    cont = cont + 1
if resultado:
    print("primo")
else:
    print("não primo")'''
