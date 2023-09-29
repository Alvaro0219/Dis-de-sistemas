from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def calcular_precio(self):
        pass

class Producto(Component):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def calcular_precio(self):
        return self.precio

class Caja(Component):
    def __init__(self, nombre, elementos):
        self.nombre = nombre
        self.elementos = elementos

    def calcular_precio(self):
        total = 0
        for elemento in self.elementos:
            total += elemento.calcular_precio()
        return total

# Crear productos
producto1 = Producto("Producto 1", 10)
producto2 = Producto("Producto 2", 15)
producto3 = Producto("Producto 3", 20)
producto4 = Producto("Producto 4", 25)

# Crear cajas y agregar productos
caja1 = Caja("Caja 1", [producto1, producto2])
caja2 = Caja("Caja 2", [caja1, producto3])
caja3 = Caja("Caja 3", [producto4])
caja4 = Caja("Caja 4", [caja2, caja3])

# Calcular el precio total utilizando el patrón Composite
precio_total = caja4.calcular_precio()
print("Precio total de todos los productos:", precio_total)

#Ejemplo de codigo sin aplicar el patron
"""class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Caja:
    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []

    def calcular_precio(self):
        total = 0
        for elemento in self.elementos:
            if isinstance(elemento, Producto):
                total += elemento.precio
            elif isinstance(elemento, Caja):
                total += elemento.calcular_precio()
        return total"""