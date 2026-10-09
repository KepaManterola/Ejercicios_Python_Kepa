HH = int(input("Hora de salida: "))
MM = int(input("Minutos de salida: "))
SS = int(input("Segundos de salida: "))
T = int(input("Tiempo de viaje en segundos: "))

total = HH * 3600 + MM * 60 + SS + T

hora = (total // 3600) % 24
minutos = (total % 3600) // 60
segundos = total % 60

print("Hora de llegada:", hora, ":", minutos, ":", segundos)