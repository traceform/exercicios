#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
qtd_notas = 4
nome_arquivo = 'media_bimestral.txt'


def coleta_nome():
    while True:
        try:
            nome = input("Digite o nome do aluno: ")
            break
        except Exception as e:
            print(f"Erro: {e}")
    nome_sanitizado = nome.strip().split()
    nome_final = ''
    for i in nome_sanitizado:
        nome_final += ' ' + i
    return nome_final.strip()

def valida_nome():
    nome = coleta_nome()
    while True:
        try:
            nome_correto = input(f"Nome digitado: {nome}\nO nome acima está correto (S/N)? ").strip().lower()
            if nome_correto.startswith('n'):
                nome = coleta_nome()
            elif nome_correto.startswith('s'):
                break
            else:
                print("Erro! Digite apenas Sim ou Não.")
        except Exception as e:
            print(f"Erro: {e}")
    return nome

def coleta_notas():
    notas = list()
    for n in range(qtd_notas): # conta de 1 a 4
        while True: # loop infinito de validação
            try:
                nota = float(input(f"Digite a nota {n+1}: "))
                notas.append(nota)
                break
            except ValueError as e:
                print(f"Número inválido! Erro: {e}")
    return notas

def calcula_media_bimestral(notas):
    return sum(notas)/len(notas)

def salva_registro(nome, notas, media):
    with open(nome_arquivo, 'w', encoding='utf8') as arquivo:
        while True:
            try:
                nome = valida_nome()
                notas = coleta_notas()
                media = calcula_media_bimestral(notas)
                arquivo.write(f"Nome: {nome}, Notas: {notas}, Média Bimestral: {media}")
            except KeyboardInterrupt:
                print("Programa encerrado")
                quit()

'''
def master():
    nome = valida_nome()
    notas = coleta_notas()
    media = calcula_media_bimestral(notas)
    salva_registro(nome, notas, media)
    print(f"A média bimestral é {media}")

master()
'''
