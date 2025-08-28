def entradaDados(qtdNotas):
    notas = []
    for n in range(1, qtdNotas+1, 1):
        invalido = True
        while invalido:
            try:
                nota = float(input(f"Informe a sua nota {n}: "))
                notas.append(nota)
                invalido = False
            except:
                print("ERRO: Número inválido!")
    return notas

def calculaMedia(notas):
    soma = 0
    for n in notas:
        soma += n
    media = soma / len(notas)
    return media

invalido = True
while invalido:
    try:
        qtdNotas = int(input("Quantas notas? "))
        invalido = False
    except:
        print("ERRO: Número inválido! Digite um número inteiro.")

print(calculaMedia(entradaDados(qtdNotas)))