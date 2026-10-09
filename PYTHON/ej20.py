monedas2 = int(input("¿Cuántas monedas de 2€ tienes? "))
monedas1 = int(input("¿Cuántas monedas de 1€ tienes? "))
monedas50 = int(input("¿Cuántas monedas de 50 céntimos tienes? "))
monedas20 = int(input("¿Cuántas monedas de 20 céntimos tienes? "))
monedas10 = int(input("¿Cuántas monedas de 10 céntimos tienes? "))

total = (monedas2 * 200) + (monedas1 * 100) + (monedas50 * 50) + (monedas20 * 20) + (monedas10 * 10)

euros = total // 100
centimos = total % 100

print("Tienes", euros, "euros y", centimos, "céntimos.")