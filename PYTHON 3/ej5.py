letra = input("Introduce un carácter: ")

while letra != " ":
    if letra.lower() in "aeiou":
        print("VOCAL")
    else:
        print("NO VOCAL")

    letra = input("Introduce un carácter: ")