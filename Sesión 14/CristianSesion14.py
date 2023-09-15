class Producto:

    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad


class ProductoFisico(Producto):


    def __init__(self, nombre, precio, cantidad, peso, dimensiones):
        super().__init__(nombre, precio, cantidad)
        self.peso = peso
        self.dimensiones = dimensiones


class ProductoDigital(Producto):

    def __init__(self, nombre, precio, cantidad, tamanio):
        super().__init__(nombre, precio, cantidad)
        self.tamanio = tamanio


class Inventario:

    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
 
        self.productos.append(producto)

    def actualizar_cantidad_producto(self, nombre, cantidad):

        producto = self.buscar_producto(nombre)
        if producto is not None:
            producto.cantidad = cantidad

    def eliminar_producto(self, nombre):

        producto = self.buscar_producto(nombre)
        if producto is not None:
            producto.remove(nombre)

    def buscar_producto(self, nombre):

        for producto in self.productos:
            if producto.nombre == nombre:
                return producto

        return None
