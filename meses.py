meses = {1:'Janeiro',2:'Fevereiro',3:'Março',4:'Abril',5:'Maio',6:'Junho',7:'Julho',8:'Agosto',9:'Setembro',10:'Outubro',11:'Novembro',12:'Dezembro'}

invalido = True                                                                       # Criação da variável para controle da repetição do while
while invalido:
    try:
        mes = int(input("Digite o dígito referente a um mês: "))                      # Pede, recebe e armazena o valor digitado pelo usuário na variável 'mes'
        if 0 < mes < 13 and mes is not float:                                         # Valida o número (é inteiro, entre 1 e 12)
            print(f"O mês é {meses.get(mes)}.")                                       # Usa o número como chave para pegar o valor certo no dicionário
            invalido = False                                                          # Encerra a repetição
        else:
            raise ValueError                                                          # Se o número não estiver entre 1 e 12 e/ou não for inteiro, chama um erro para alertar o usuário do que causou o erro
    except ValueError:
        print("ERRO: Número inválido! Só são aceitos números inteiros de 1 a 12.")    # Avisa ao usuário que há um erro e repete o while do início, também ocorre quando algum caractere não-numérico é digitado no input (como letras) ao invés de quebrar o código abruptamente, validando o input.
