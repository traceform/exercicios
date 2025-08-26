# Escrever um código python que baseado no valor da variável armazene um texto, quantifique a quantidade de vogais e consoantes.
vogais = ['a', 'e', 'i', 'o', 'u']
vogaisAcentuadas = ['á', 'é', 'í', 'ó', 'ú', 'à', 'â', 'ê', 'ô', 'ã', 'õ', 'ü']
consoantes = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

texto = "Você está no meu coração!"
qtdVogais = 0
qtdConsoantes = 0

for l in texto.lower():
    if l in vogais or l in vogaisAcentuadas:
        qtdVogais += 1
    elif l in consoantes or l == 'ç':
        qtdConsoantes += 1

print(f"Texto: {texto}")
print(f"Quantidade total de caracteres: {len(texto)}")
print(f"Quantidade de vogais: {qtdVogais}")
print(f"Quantidade de consoantes: {qtdConsoantes}")
