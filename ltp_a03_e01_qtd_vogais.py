# Escrever um código python que baseado no valor da variável que armazene o seu nome, quantifique a quantidade de vogais.
vogais = ['a', 'e', 'i', 'o', 'u']
vogaisAcentuadas = ['á', 'é', 'í', 'ó', 'ú', 'à', 'â', 'ê', 'ô', 'ã', 'õ', 'ü']

name = "José Carioca"
qtdVogais = 0

for l in name:
    if l in vogais or l in vogaisAcentuadas:
        qtdVogais += 1
print(f"Quantidade de vogais: {qtdVogais}")
