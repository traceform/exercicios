print("=" * 14 , "CALCULADORA DE ÁREA E PERÍMETRO" , "=" * 14)
lado = float(input("Digite o valor correspondente ao lado  do quadrado em metros: ").strip()) #Tira os espaços, caso haja algum
ladoStr = str(lado) #Guarda a string da variável lado na variável ladoStr
'''Preciso separar os inteiros dos flutuantes para evitar que o ponto flutuante '.' apareça sem a necessidade, como no caso de um
número inteiro, ex.: '1.0'. Então pensei em verificar se a string '.0' é encontrada na ladoStr, pois isso certamente significaria
que o número é inteiro, no entanto é possível que haja um float de valor 10.08, por exemplo.
    Então resolvi usar o comando .find() que funciona assim: variavel.find('caractere'). Assim é possível encontrar a posição de
um caractere na string de acordo com a posição do índice, cuja contagem começa do 0, exemplo: 'artesão' tem 7 caracteres, portanto
len() resultará em 7. No entanto se eu quiser descobrir a posição do caractere 'a', .find() me retornará o valor 0, pois 'a' é o
primeiro caractere da string enquanto o último, 'o', é o número 6 do índice.
    Tentei então usar o .rfind() que conta da esquerda para a direita. Dessa forma, no caso de uma variável cujo valor é 'amena'
(5 caracteres) o resultado de .find('a') seria 0 e o de .rfind('a') seria 4, pois apesar de ambos procurarem 'a', eles o procuram
em sentidos diferentes, mas como pode ver, não retornam o valor da posição em que encontraram e sim a posição do índice.
    Então, por fim, descobri que se eu pegasse o total de caracteres (5 segundo o exemplo anterior) e calculasse a diferença quanto
ao valor do índice onde o '.' está (o último 'a', índice 4 no exemplo anterior) eu encontraria a quantidade de caracteres restantes 
para alcançar o fim da string, ou seja, len(exemplo) - exemplo.rfind('a') resultará em 1, que é a posição do 'a' final quando 
contamos da direita para a esquerda. Provavelmente há uma forma mais fácil de fazer isso, mas essa foi a que fiz funcionar.'''
if '.0' in ladoStr and len(ladoStr) - ladoStr.rindex('.') == 2:
    lado = int(lado) #Converte o valor da variável lado (não confundir com ladoStr) de float para inteiro
    print(f"perímetro: {lado * 4} - área: {lado ** 2}") #Imprime os valores requisitados, não precisei criar variáveis extras
else:
    print(f"perímetro: {lado * 4:.2f} - área: {lado ** 2:.2f}") #Faz o mesmo, porém com apenas duas casas decimais para floats
