numeraso = input("Ingresa un número (ENTER para terminar): ")

if numeraso == "":
    print("No se ingresaron números.")
else:
    minimo = float(numeraso)
    maximo = float(numeraso)

    while True:
        numeraso = input("Ingresa un número (ENTER para terminar): ")
        if numeraso == "":
            break
        numero = float(numeraso)

        if numero < minimo:
            minimo = numero
        if numero > maximo:
            maximo = numero

    print("Número mínimo:", minimo)
    print("Número máximo:", maximo)
