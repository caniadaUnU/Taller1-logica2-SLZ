suma = 0
contador = 0

monto = float(input("Ingresa un monto (0 para terminar): "))

while monto != 0:
    suma = suma + monto
    contador = contador + 1
    monto = float(input("Ingresa un monto (0 para terminar): "))

print("Cantidad de montos ingresados:", contador)
print("Suma total:", suma)
