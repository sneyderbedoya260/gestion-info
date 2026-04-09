nota = int(input("Ingrese la calificación (0-100): "))

if 0 <= nota <= 100:
    if nota >= 90:
        print("Calificación: A")
    elif nota >= 80:
        print("Calificación: B")
    elif nota >= 70:
        print("Calificación: C")
    elif nota >= 60:
        print("Calificación: D")
    else:
        print("Calificación: F")
else:
    print("Nota fuera de rango.")