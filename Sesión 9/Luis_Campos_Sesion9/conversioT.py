
datos_grados = {}
while True:
    num_grados = int(input('ingrese la cantidad numero de grados Celsius:'))
    for it in range(1, num_grados + 1):
        celsius = int(input(f"Ingrese la temperatura a convertir {it}: "))
        faherenheit = (celsius * 9 / 5) + 32
        datos_grados[celsius] = faherenheit
    1
    print('\nDatos de los grados convertidos:')
    for celsius,faherenheit, in datos_grados.items():
        print(f'celsius: {celsius},faherenheit:{faherenheit},')

    continuar = input('¿Desea realizar otra conversion? (s/n)')
    
    if continuar != 's':
        break
    
