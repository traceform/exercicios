nomeCliente = input("Digite o nome do cliente: ").title()
diaVencimento = int(input("Digite o dia do vencimento: "))
def funcao_fatura(): #fiz a função para evitar repetir esta parte
    valorFatura = input("Digite o valor da fatura: R$")
    print(f"Olá, {nomeCliente}")
    print(f"A sua fatura com vencimento em {diaVencimento} de {mesVencimento.title()} no valor de R$ {valorFatura} está fechada.")
if 0 < diaVencimento <= 31: #um mês não pode ter dias negativos ou maiores que 31
    mesVencimento = input("Digite o mês do vencimento por extenso: ").strip().lower() #tratamento de dados
    if mesVencimento in ['abril', 'junho', 'setembro', 'novembro'] and diaVencimento <= 30: #meses de 30 dias
        funcao_fatura()
    elif mesVencimento in ['janeiro', 'março', 'maio', 'julho', 'agosto', 'outubro', 'dezembro']: #meses de 31
        funcao_fatura()
    elif mesVencimento == 'fevereiro' and diaVencimento <= 29: #fevereiro tem até 29 dias em ano bissexto
        funcao_fatura()
    else:
        print(f"{mesVencimento.title()} não possui {diaVencimento} dias. Tente novamente.")
else:
    print("Este dia não existe, tente novamente.")
