# Recebe texto do usuário, quebra pelo ponto e capitaliza cada frase

texto = input("Digite um texto: ")

textoSeparado = texto.split('.')
#print(textoSeparado)
for i in textoSeparado:
    #print(i)
    if i == '':
        continue
    print(i.strip().capitalize() + '.')
