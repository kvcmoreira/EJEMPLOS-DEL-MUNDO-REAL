# Clase Producto
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} - ${self.precio} ({self.cantidad} disponibles)"

# Clase CarritoDeCompra
class CarritoDeCompra:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto, cantidad):
        if producto.cantidad >= cantidad:
            self.productos.append((producto, cantidad))
            producto.cantidad -= cantidad
            print(f"Agregado {producto.nombre} x{cantidad} al carrito.")
        else:
            print(f"No hay suficiente stock de {producto.nombre}.")

    def mostrar_carrito(self):
        print("Carrito de Compra:")
        for producto, cantidad in self.productos:
            print(f"{producto.nombre} x{cantidad} - ${producto.precio * cantidad}")

    def calcular_total(self):
        total = sum(producto.precio * cantidad for producto, cantidad in self.productos)
        return total

# Clase Pedido
class Pedido:
    def __init__(self, carrito):
        self.productos = carrito.productos
        self.total = carrito.calcular_total()

    def mostrar_pedido(self):
        print("Pedido Realizado:")
        for producto, cantidad in self.productos:
            print(f"{producto.nombre} x{cantidad} - ${producto.precio * cantidad}")
        print(f"Total a Pagar: ${self.total}")

# Ejemplo de uso
if __name__ == "__main__":
    producto1 = Producto("Laptop", 1200, 10)
    producto2 = Producto("Smartphone", 800, 20)
    producto3 = Producto("Tablet", 600, 15)

    carrito = CarritoDeCompra()
    carrito.agregar_producto(producto1, 1)
    carrito.agregar_producto(producto2, 2)
    carrito.agregar_producto(producto3, 1)

    carrito.mostrar_carrito()
    print(f"Total del carrito: ${carrito.calcular_total()}")

    pedido = Pedido(carrito)
    pedido.mostrar_pedido()
