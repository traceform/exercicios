def entradaDados(qtdNotas):
    notas = []
    for n in range(1, qtdNotas+1, 1):
        nota = float(input(f"Informe a sua nota {n}: "))
        notas.append(nota)
    return notas

def calculaMedia(notas):
    soma = 0
    for n in notas:
        soma += n
    media = soma / len(notas)
    return media

print(calculaMedia(entradaDados(int(input("Quantas notas? ")))))