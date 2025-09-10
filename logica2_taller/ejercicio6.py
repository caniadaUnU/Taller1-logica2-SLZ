N = int(input("¿Cuántos números vas a ingresar? "))

suma = 0
contador = 0

for i in range(N):
    numero = float(input("Ingresa un número (0 para terminar): "))
    if numero == 0:
        break 
    suma = suma + numero
    contador = contador + 1

if contador > 0:
    promedio = suma / contador
    print("El promedio es:", promedio)
else:
    print("No se ingresaron números para calcular el promedio.")