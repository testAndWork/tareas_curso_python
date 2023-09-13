
nun_comprados = int(input('ingrese el numero de productos a comprar:'))
datos_compra = []
for it in range(1,nun_comprados + 1):
    datos_compra.append(input('ingresa los productos a comprar:'))
1
setconvert = set(datos_compra)
print(f'los productos a comprar son: {setconvert}')
