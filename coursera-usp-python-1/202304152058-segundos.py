segundosTotal = int(input("Por favor, entre com um número de segundos que deseja converter: "))
dias = segundosTotal // 86400 # 1 day = 3600 seconds x 24 hours = 86400 seconds
# horas = segundosTotal // 3600 # 1 hour = 60 minutes x 60 seconds = 3600 seconds
# minutos = segundosTotal // 60 # 1 minute = 60s
segundosRestantes1 = segundosTotal % 86400 # pego o resto (segundos) da divisão para dia
horasRestantes = segundosRestantes1 // 3600 # calculo quantas horas é possível obter
segundosRestantes2 = segundosRestantes1 % 3600 # calculo o resto (segundos) da divisão anterior
minutosRestantes = segundosRestantes2 // 60 # calculo quantos minutos é possível obter
segundosRestantes3 = segundosRestantes2 % 60 # calculo quantos segundos sobraram
print(f"{dias} dias, {horasRestantes} horas, {minutosRestantes} minutos e {segundosRestantes3} segundos")
# print(f"TOTAL: {dias} dias, {horas} horas, {minutos} minutos e {segundosTotal} segundos.")
