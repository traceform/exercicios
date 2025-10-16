'''
arquivo = open('contatos.txt', 'w')
arquivo.write("A - 111\nB - 222\nC - 333\n")
arquivo.close()

arquivo = open('contatos.txt', 'a')
arquivo.write("D - 444\nE - 555\nF - 666")
arquivo.close()
'''

'''
arquivo_original = open('contatos.txt', 'r')
texto = []
for linha in arquivo_original:
    if 'A' in linha:
        texto.append(linha.replace('A','Z'))
    else:
        texto.append(linha)
arquivo_original.close()

arquivo_final = open('contatos.txt', 'w')
for linha in texto:
    arquivo_final.write(linha)
arquivo_final.close()
'''

'''#descobrir como o seek funciona
arquivo = open('contatos.txt', 'a')
print(arquivo.seek()))
arquivo.close()
'''

'''
arquivo = open('texto.txt', 'w')
arquivo.close()

arquivo = open('texto.txt', 'a', encoding='utf8')
frases = list()
frases.append('TreinaWeb \n')
frases.append('Python \n')
frases.append('Arquivos \n')
frases.append('Django \n')

arquivo.writelines(frases)
arquivo.close()

arquivo = open('texto.txt','r')
print(f">>>read:\n{arquivo.read()}")
arquivo.seek(0) # manda começar do início, pois o de cima já fez com que o ponteiro chegase ao fim
print(f">>>readline:\n{arquivo.readline(3)}") # conta por caractere
arquivo.seek(0) # tem que usar pra voltar pro início, ou então vai começar de onde parou anteriormente
print(f">>>readlines:\n{arquivo.readlines()}") # gera uma lista com as linhas do arquivo
arquivo.close()
'''

'''
with open('texto.txt', 'r') as arquivo:
    texto = arquivo.read()
print(texto)
'''

f = None
try:
    f = open('teste_erro.txt','r')
    texto = f.read()
except Exception as x:
    print(x)
finally:
    print('Tudo ok')

# 1. Cada operação de acesso ao arquivo deve ser feita separadamente, caso contrário dá erro
#     Exemplo, tentar escrever com acesso de leitura, tentar ler com acesso de escrita.
# 2. Cada vez que se usa 'w', o arquivo mencionado é criado do zero ou sobrescrito
