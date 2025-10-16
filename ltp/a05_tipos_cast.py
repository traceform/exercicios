### INT: remove o floating point, não arredonda
print("====INT====")
v = int(10.5)
print(v)

v = int(10.9)
print(v)

v = int(True) # vira 1
print(v)

v = int(False) # vira 0
print(v)

### BOOLEANO: Retorna False se for 0, 0.0, '' ou None e True se tiver algum valor, seja 1, positivo e negativo, '0', 'False', etc
print("====BOOLEAN====")
v = bool(True)
print(v)

v = bool(False)
print(v)

v = bool(0) # vira False
print(v)

v = bool(1) # vira True
print(v)

v = bool(10)
print(v)

v = bool(-1)
print(v)

v = bool(None)
print(v)

v = bool("0")
print(v)

### STRING
print("====STRING====")

v = str(True)
print(v)

v = str(False)
print(v)

t = "O Senac é Legal. e a unb não"

# Métodos:
print(t.lower()) # Método sem parâmetro
print(t.upper())
print(t.capitalize()) # Só capitaliza o primeiro caractere da string enquanto descapitaliza o resto
print(t.replace('é','e')) # Método com parâmetro
print(t.replace('é','e').upper()) # Concatenação de métodos
    # Cuidado: o que aconteceria se o resultado do primeiro método for None?
print(t.split(' ')) # Quebra a string, separando por espaços
print(t.split('.')) # Quebra a string, separando por pontos
print(t.split())
t = "    O Senac é Legal. e a unb não  "
print([t.strip()])
print([t.rstrip()])
print([t.lstrip()])
print([t.rsplit()])

### Métodos de string que começam com IS, resultado é sempre booleano
print("12A".isdigit())
print("12A".isnumeric())
print("12A".isprintable())
print("Aa".islower())
print("a".islower())
print("a".isalpha())
print("a1".isalpha())
print("a1".isalnum())

print('123'.zfill(8)) # Como seria guardada a senha de banco num banco de dados, blockada. Pouco utilizado.
