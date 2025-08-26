count, notaTotal = 0, 0
while count < 4:
	count = count + 1
	nota = float(input(f"Digite a {count}º nota: "))
	notaTotal = notaTotal + nota
print(f"A média aritmética é {notaTotal / 4}")
