numero = int(input("Dime un número de dos cifras: "))

decenas = numero // 10
unidades = numero % 10

invertido = unidades * 10 + decenas

print("El número invertido es:", invertido)