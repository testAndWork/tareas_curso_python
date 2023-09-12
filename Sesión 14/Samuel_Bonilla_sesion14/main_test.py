import modulo_inventario as mi

inventario = mi.Inventario()

producto_fisico = mi.ProductoFisico('caja', 10, 4, 20, (4, 5, 5))

producto_digital = mi.ProductoDigital('Foto', 100, 10, 40)

#Agregar productos a inventarios

inventario.agregar_productos(producto_fisico)
inventario.agregar_productos(producto_digital)
    
#Actualizar productos

inventario.actualizar_cantidad_producto('caja',20)
for producto in inventario.productos:
    print(producto.nombre)
    print(producto.cantidad)