print("=" * 13 , "CALCULADORA DE MÉDIA" , "=" * 13)
notasTotal = input("Total de notas para calcular a média: ")
if notasTotal.replace('.','').isnumeric() == False or notasTotal.isalpha() == True:
	print("Caractere inválido!")
	exit()
if float(notasTotal) < 2:
	print("Para calcular a média são necessários pelo menos dois números!")
else:
	cont, soma = 0, 0
	while cont < int(notasTotal):
		cont = cont + 1
		nota = float(input(f"Nota {cont}: "))
		soma = soma + nota
	print(f"Média: {soma / cont:.1f}")
