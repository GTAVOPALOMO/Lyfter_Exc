"""
Cree una clase Product con:
Nombre, precio y cantidad
Cree una clase Inventory que:
Guarde productos en una lista
Tenga métodos para:
Agregar un producto
Mostrar todos los productos
Calcular el valor total del inventario
"""
class Product:
    def __init__(self, p_price, p_name, p_quantity):
        self.price = p_price
        self.name = p_name
        self.quantity = p_quantity

class Inventory:
    def __init__(self):
        self.product_list = []
    def add_product(self,p_product: Product):
        self.product_list.append(p_product)
    def show_products(self):
        for prod in self.product_list:
            print(f"Nombre: {prod.name}, Precio: {prod.price}, Cantidad: {prod.quantity}")
    def total_amount(self):
        return sum((prod.price * prod.quantity) for prod in self.product_list)