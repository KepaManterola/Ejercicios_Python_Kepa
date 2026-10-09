parcial1 = float(input("Dime la primera calificación parcial: "))
parcial2 = float(input("Dime la segunda calificación parcial: "))
parcial3 = float(input("Dime la tercera calificación parcial: "))

examen = float(input("Dime la calificación del examen final: "))
trabajo = float(input("Dime la calificación del trabajo final: "))

promedio = (parcial1 + parcial2 + parcial3) / 3

nota_final = (promedio * 0.55) + (examen * 0.30) + (trabajo * 0.15)

print("Tu calificación final es:", nota_final)