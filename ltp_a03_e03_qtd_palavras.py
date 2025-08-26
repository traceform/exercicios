# Escrever um código python que armazene um texto e, baseado no valor da variável, quantifique a quantidade de palavras.
texto = "senac é legal".strip().split()
#print(texto)
print(len(texto))

'''Código do professor:
texto = "   senac          e unb      ".upper().strip() #depende da regra de negócio

print(texto)

qtd = 0
for c in texto.split(' '): #split fica aqui porque muda o tipo da variável, depende da regra de negócio
    if not c == ' ':
        qtd += 1

print("O valor de palavras: ", str(qtd))

'''
