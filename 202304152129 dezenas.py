num = input("Digite um número inteiro: ")
if len(num) == 1:
	print(f"O dígito das dezenas é 0")
else:
	print(f"O dígito das dezenas é {int(num[-2])}")
