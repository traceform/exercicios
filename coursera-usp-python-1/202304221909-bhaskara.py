from math import sqrt
a = float(input("Digite o valor de a: "))
if a == 0:
    print("A equação não pode ser quadrática se a for 0!")
else: #f(x) = ax² + bx + c, a != 0
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    delta = b ** 2 - (4 * a * c) #delta = b² - 4ac
    if delta < 0:
        print("esta equação não possui raízes reais")
    else: #x = (-b +/- sqrt(delta) / 2a)
        x1 = ((-b) + sqrt(delta)) / (2 * a) #raiz 1
        x2 = ((-b) - sqrt(delta)) / (2 * a) #raiz 2
        if delta > 0:
            if x1 < x2:
                print(f"as raízes da equação são {x1} e {x2}")
            else:
                print(f"as raízes da equação são {x2} e {x1}")
        else: #se delta for igual a zero, as raízes serão iguais entre si
            print(f"a raiz desta equação é {x1}")
        
#ax2 + bx + c
#se delta < 0 esta equação não possui raízes reais
#se delta == 0 a raiz desta equação é X
#se delta > 0 a raiz dupla desta equação é X
#se delta > 0 as raízes da equação são X e Y
    #se diferentes, em ordem crescente
