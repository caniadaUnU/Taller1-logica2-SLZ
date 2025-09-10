bandera = False

nombre = input("Ingresa un nombre (deja vacío para terminar): ")

while nombre != "":
    primera_letra = nombre[0]
    if primera_letra == "A" or primera_letra == "a":
        bandera = True
    nombre = input("Ingresa un nombre (deja vacío para terminar): ")

if bandera:
    print("Se encontró un nombre que empieza con 'A'.")
else:
    print("No se encontró ningún nombre que empiece con 'A'.")
