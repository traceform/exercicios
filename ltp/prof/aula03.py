texto = "   senac         e unb   "
print(texto)

print(texto)

print(texto[0])

qtd = 0
vogais = ['A', 'E', 'I', 'O', 'U']
for c in texto:
    if c in vogais:
        qtd += 1

print("O valor de vogais: " + str(qtd))

qtd = 0
for c in texto.upper().strip().split(' '):
    if not c == '':
        qtd +=1

print("O valor de palavras: " + str(qtd))

mes = int(input("Informe o mês de modo numerico: ")) -1
meses = ["janeiro", "fevereiro"]
print(meses[mes])
