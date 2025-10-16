def entraDados():
    nota01 = float(input("Informa a nota 01:"))
    nota02 = float(input("Informa a nota 02:"))
    nota03 = float(input("Informa a nota 03:"))
    nota04 = float(input("Informa a nota 04:"))

    return nota01, nota02, nota03, nota04

def calculaMedia(nota01, nota02, nota03, nota04):
    return (nota01 + nota02 + nota03 + nota04) / 2

nota01, nota02, nota03, nota04 = entraDados()

media = calculaMedia(nota01, nota02, nota03, nota04)

print(media)