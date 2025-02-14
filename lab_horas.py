#lab 3 - prevendo fim de jogo - correção



hour = int(input("Hora de início (horas): "))
mins = int(input("Hora de início (minutos): "))
dura = int(input("Duração do evento (minutos): "))
mins = mins + dura # encontre um total de todos os minutos
print("mins",mins)
hour = hour + mins // 60 # encontre um número de horas escondido em minutos e atualize a hora
print("hour",hour)
mins = mins % 60 # minutos corretos para cair no intervalo (0..59)
print("mins",mins)
hour = hour % 24 # horas corretas para cair no intervalo (0..23)
print("hour",hour)
print("Final - ",hour, ":", mins, sep='')
