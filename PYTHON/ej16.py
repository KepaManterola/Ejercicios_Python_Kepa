d = float(input("Dime la distancia entre los vehículos (km): "))
v1 = float(input("Dime la velocidad del vehículo de delante (km/h): "))
v2 = float(input("Dime la velocidad del vehículo de detrás (km/h): "))

tiempo_horas = d / (v2 - v1)
tiempo_minutos = tiempo_horas * 60

print("El vehículo más rápido alcanzará al otro en", tiempo_minutos, "minutos")