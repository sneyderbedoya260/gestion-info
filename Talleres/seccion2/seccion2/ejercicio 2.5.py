categoria = input("Ingrese su categoría (A, B, C): ").upper()
monto = float(input("Ingrese el monto de la compra: "))

descuento = 0

if categoria == "A":
    descuento = 0.20
elif categoria == "B":
    descuento = 0.15
elif categoria == "C":
    descuento = 0.10

ahorro = monto * descuento
total = monto - ahorro

print(f"Descuento aplicado: ${ahorro:.2f}")
print(f"Total a pagar: ${total:.2f}")