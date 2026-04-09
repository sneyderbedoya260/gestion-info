inventario = [
    {"nombre": "Laptop", "precio": 2500, "stock": 10},
    {"nombre": "Mouse", "precio": 50, "stock": 100},
    {"nombre": "Teclado", "precio": 120, "stock": 50}
]

producto_buscar = input("Ingrese el nombre del producto a actualizar: ")

for producto in inventario:
    if producto["nombre"].lower() == producto_buscar.lower():
        nuevo_precio = float(input("Ingrese el nuevo precio: "))
        producto["precio"] = nuevo_precio
        print("Precio actualizado correctamente.")
        break
else:
    print("Producto no encontrado.")

print("Inventario actualizado:")
for producto in inventario:
    print(producto)