from math import sqrt
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
delta = float(b ** 2 - 4 * a * c)
if delta < 0:
	print("Esta equação não possui raízes reais.")
else:
	x1 = ((-b) + sqrt(delta)) / (2 * a)
	x2 = ((-b) - sqrt(delta)) / (2 * a)
	if x1 != x2:
		if x1 < x2:
			print(f"As raízes da equação são: {x1} e {x2}")
		else:
			print(f"As raízes da equação são: {x2} e {x1}")
	else:
		print(f"A raiz desta equação é {x1}")

'''
f(x) = ax² + bx + c, a != 0
x = (-b +/- sqrt(delta) / 2a)
delta = b² - 4ac
delta = 83927942
sqrt(delta)
delta < 0 "Esta equação não possui raízes reais."
delta == 0 "A raiz desta equação é {raiz}"
delta > "As raízes da equação são: {raiz1} e {raiz2}"'''
