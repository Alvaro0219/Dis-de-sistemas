class Servicio:
    def __init__(self, nombre, precio, descripcion, ubicacion, fecha_hora):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.ubicacion = ubicacion
        self.fecha_hora = fecha_hora

class GestorPagos:
    def calcular_total(self, servicio, cantidad_personas):
        total = servicio.precio * cantidad_personas
        return total

class Controller:
    def __init__(self):
        self.servicios = {
            1: Servicio("Tour por la ciudad", 1500, "Un recorrido por los puntos más destacados de la ciudad", "Plaza principal", "15/06/2023 10:00"),
            2: Servicio("Visita guiada al museo", 800, "Un recorrido guiado por las exposiciones del museo", "Museo de Arte Moderno", "20/06/2023 14:00"),
            3: Servicio("Paseo en bote por el lago", 2000, "Un paseo en bote para disfrutar del paisaje del lago", "Lago Central", "25/06/2023 16:00")
        }
    
    def obtener_servicios(self):
        return self.servicios
    
    def mostrar_servicios(self):
        print("SERVICIOS DISPONIBLES")
        print("-"*30)
        for id_servicio, servicio in self.servicios.items():
            print(f"ID: {id_servicio} - Nombre: {servicio.nombre} - Precio: ${servicio.precio} - Fecha y hora: {servicio.fecha_hora}")
        print("-"*30)

class Interfaz:
    controller = Controller()

    def menu(self):
        self.opcion = 0

        while self.opcion<1 or self.opcion>2:
            print("\n¿Qué acción desea realizar?")
            print("1. Contratar servicio")
            print("2. Salir")
            self.opcion = int(input("Ingrese el número correspondiente a su opción: "))
        
        return self.opcion
    
    def seleccionar_servicio(self):
        servicios = self.controller.obtener_servicios()
        servicio = None
        while servicio is None:
            id_servicio = int(input("Seleccione el ID del servicio que desea contratar: "))
            servicio = servicios.get(id_servicio)
            if servicio is None:
                print("El servicio seleccionado no es válido.")
        return servicio
    
    def ingresar_cantidad_personas(self):
        while True:
            try:
                cantidad_personas = int(input("Ingrese la cantidad de personas que utilizarán el servicio: "))
                if cantidad_personas <= 0:
                    print("La cantidad de personas debe ser mayor a cero.")
                else:
                    return cantidad_personas
            except ValueError:
                print("Debe ingresar un número entero válido.")
    
    def ingresar_datos_personas(self, cantidad_personas):
        datos_personas = []
        for i in range(cantidad_personas):
            print(f"Ingrese los datos de la persona {i + 1}:")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            dni = input("DNI: ")
            datos_personas.append({"nombre": nombre, "apellido": apellido, "dni": dni})
        return datos_personas
    
    def mostrar_datos_bancarios(self,total):
        print("Estos son los datos bancarios para realizar la transferencia:")
        print("---------------------------")
        print(f"PRECIO = ${total}")
        print("CBU = 00005478982242312872")
        print("ALIAS= ALIAS.TURISMO")
        print(f"NRO.CUENTA = 0025478936")
        print("*Una vez confirmado el pago recibirá un comprobante por email")
        print("---------------------------")


def main():
    controller = Controller()
    gestor = GestorPagos()
    interfaz = Interfaz()

    opcion = interfaz.menu()

    if opcion==1:
        controller.mostrar_servicios()
        servicio = interfaz.seleccionar_servicio()
        cant_personas = interfaz.ingresar_cantidad_personas()
        datos_personas = interfaz.ingresar_datos_personas(cant_personas)
        total = gestor.calcular_total(servicio, cant_personas)
        interfaz.mostrar_datos_bancarios(total)
    elif opcion==2:
        print("Gracias por utilizar nuestro servicio")
    else:
        pass

if __name__ == '__main__':
    main()