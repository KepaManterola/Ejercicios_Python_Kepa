sueldo = float(input("Dime tu sueldo base: "))

venta1 = float(input("Dime el importe de la venta 1: "))
venta2 = float(input("Dime el importe de la venta 2: "))
venta3 = float(input("Dime el importe de la venta 3: "))

comision1 = venta1 * 0.10
comision2 = venta2 * 0.10
comision3 = venta3 * 0.10

comisiones = comision1 + comision2 + comision3

total = sueldo + comisiones

print("Comisiones:", comisiones, "€")
print("Total a recibir:", total, "€")