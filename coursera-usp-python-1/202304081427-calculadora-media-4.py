print("=" * 13 , "CALCULADORA DE MÉDIA" , "=" * 13)
notasTotal = input("Total de notas para calcular a média: ").strip()
alvo = notasTotal
verificaInt = alvo.isnumeric() == False or alvo.isalpha() == True
if verificaInt == True:
	print("Caractere inválido!")
if float(notasTotal) < 2:
	print("Para calcular a média são necessários pelo menos dois números!")
else:
	cont, soma = 0, 0
	while cont < float(notasTotal):
		cont = cont + 1
		nota = input(f"Nota {cont}: ").strip()
		alvo = nota
		verificaFloat = alvo.replace('.','').isnumeric() == False or alvo.isalpha() == True
		if verificaFloat == False:
			soma = soma + float(nota)
		elif verificaFloat == True:
			print("Caractere inválido!")
			exit()
	print(f"Média: {soma / cont:.1f}")
