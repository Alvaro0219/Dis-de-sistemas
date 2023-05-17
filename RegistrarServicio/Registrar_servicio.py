import re

# tipo de dato que representa un servicio y que puede ser utilizado en el programa para almacenar y manipular información sobre un servicio.
class Servicio:
    def __init__(self, datos):
        #Metodo constructor->inicializa los valores de una instancia
        self.titulo = datos["titulo"]
        self.descripcion = datos["descripcion"]
        self.ubicacion = datos["ubicacion"]
        self.precio = datos["precio"]
        self.fecha_hora = datos["fecha_hora"]
        self.tipo = datos["tipo"]

        
class Interfaz:
    #MENU DEL SITIO WEB
    def mostrar_menu(self):
        menu = """
        BIENVENIDO A TURISMO
        1- Registrar servicio
        2- Contratar servicio
        3- Salir

        SELECCIONE UNA OPCION:
        """
        self.opcion = input(menu)

        while self.opcion not in ["1", "2", "3"]:
            print("Opcion incorrecta")
            self.opcion = input(menu)

        return self.opcion
    
    def registrar_servicio(self):
        print("Ingrese los siguientes datos:")
        titulo = input("Título: ")
        descripcion = input("Descripción: ")
        ubicacion = input("Ubicación: ")

        precio = input("Precio: ")
        while not re.match(r'^\d+(?:\.\d{1,2})?$', precio):
            print("Error: el precio debe ser un número válido con hasta dos decimales.")
            precio = input("Precio: ")
        precio = float(precio)

        fecha_hora = input("Fecha y Hora (DD/MM/AAAA HH:MM): ")
        while not re.match(r'^\d{2}/\d{2}/\d{4}\s\d{2}:\d{2}$', fecha_hora):
            print("Error: la fecha y hora deben estar en el formato DD/MM/AAAA HH:MM.")
            fecha_hora = input("Fecha y Hora (DD/MM/AAAA HH:MM): ")

        tipo = input("Tipo: ")

        # Comprobar que los campos obligatorios no estén en blanco
        if not titulo or not descripcion or not ubicacion or not tipo:
            print("Error: todos los campos son obligatorios.")
            return self.registrar_servicio()  # Volver a solicitar al usuario que ingrese los datos

        return {"titulo": titulo,
                "descripcion": descripcion,
                "ubicacion": ubicacion,
                "precio": precio,
                "fecha_hora": fecha_hora,
                "tipo": tipo}
    
    def mostrar_servicios(self, servicios):
        if not servicios:
            print("No hay servicios registrados")
        else:
            print("\n--------------------------------")
            print("SERVICIOS DISPONIBLES")
            for id_servicio, servicio in servicios.items():
                print(f"ID: {id_servicio} - Título: {servicio.titulo} - Descripcion: {servicio.descripcion} - Precio: {servicio.precio} - Fecha y hora: {servicio.fecha_hora}")
            print("--------------------------------")



class Controller:
    def __init__(self):
        #Diccionario de servicios->BD
        self.servicios = {}
        #Instancia de la clase interfaz
        self.interfaz = Interfaz()

    def registrar_servicio(self):
        datos = self.interfaz.registrar_servicio()
        #objeto Servicio con los datos ingresados por el usuario
        servicio = Servicio(datos)

        # ALMACENAR SERVICIO EN LA BD
        #identificador único para el nuevo servicio
        id_servicio = len(self.servicios) + 1
        #agrega el nuevo servicio a la base de datos utilizando ese identificador único como clave.
        self.servicios[id_servicio] = servicio

        print("El servicio ha sido registrado con éxito")

    def mostrar_servicios(self):
        self.interfaz.mostrar_servicios(self.servicios)

def main():
    #Instancias
    controller = Controller()
    interfaz = Interfaz()

    while True:
        opcion = interfaz.mostrar_menu()

        if opcion == "1":
            controller.registrar_servicio()
        elif opcion == "2":
            controller.mostrar_servicios()
        elif opcion == "3":
            break
        else:
            pass

if __name__ == '__main__':
    main()