QTDNOTAS = 4
NOMEARQUIVO = "notas.txt"

# recuperar as notas do aluno
def informarDados(qtdNotas):
    listaNotas = list()
    for nota in range(qtdNotas):
        try:
            valor = float(input("Informe a nota "+ str(nota+1) + ":"))
            listaNotas.append(valor)
        except:
            raise Exception("Notas Invalidas")

    return listaNotas

# realiza o calculo da média
def calculaMedia(listaNotas):
    try:
        return(sum(listaNotas) / len(listaNotas))
    except:
        raise Exception("Não foi possivel calcular a média")

# realiza a gravação do arquivo
def gravaDados(listaNotas, media):

    resultado = {
        'Notas': listaNotas,
        'Média': media
    }

    try:    
        with open(NOMEARQUIVO, 'a', encoding='utf-8') as arquivo:
            arquivo.writelines(str(resultado) + "\n")
    except:
        raise Exception("Não foi possivel gravar dados")

# ponto de inicialização do código
if __name__ == "__main__":
    try:
        listaNotas = informarDados(QTDNOTAS)

        media = calculaMedia(listaNotas)

        gravaDados(listaNotas, media)

    except Exception as e:
        print(e)