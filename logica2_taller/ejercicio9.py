nota = float(input("Ingresa una nota entre 0 y 5: "))

while nota < 0 or nota > 5:
    print("Nota inválida. Intenta de nuevo.")
    nota = float(input("Ingresa una nota entre 0 y 5: "))

print("La nota válida es:", nota)
