import math
import os

class OnlineStore:
    def __init__(self):
        self.inventory = []
        self.total_sales = 0
        
    def add_products(self, product_name, price):
        self.inventory.append(product_name)
        self.inventory.append(price)
    
    def purchase(self, product_name):
        for producto in self.inventory:
            if producto.product_name == product_name:
                return producto
    
    def show_sales(self):
        return print(f'Producto: {self.inventory}')

tienda_linea=OnlineStore()

agregar = tienda_linea.add_products('Leche', 1.50)
