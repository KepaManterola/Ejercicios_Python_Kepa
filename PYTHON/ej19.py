correctas = int(input("¿Cuántas respuestas correctas? "))
incorrectas = int(input("¿Cuántas respuestas incorrectas? "))
blanco = int(input("¿Cuántas respuestas en blanco? "))

nota = (correctas * 5) + (incorrectas * -1) + (blanco * 0)

print("La nota final es:", nota)