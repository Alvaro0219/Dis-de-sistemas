
class Interfaz:
    def pedir_cuit(self):
        return input("Ingrese su CUIT: ")

    def pedir_nombre(self):
        return input("Ingrese su nombre: ")

    def pedir_apellido(self):
        return input("Ingrese su apellido: ")

    def pedir_contraseña(self):
        return input("Ingrese una contraseña para su cuenta: ")

    def mostrar_error(self, mensaje):
        print("Error:", mensaje)

    def mostrar_exito(self, mensaje):
        print("Éxito:", mensaje)

class Guia:
    #Utilizamos self para referirnos al metodo que esta siendo creado o manipulado
    #Metodo constructor->inicializa los valores de una instancia
    def __init__(self, cuit, nombre, apellido, password):
        self.cuit = cuit
        self.nombre = nombre
        self.apellido = apellido
        self.password = password

    def __str__(self):
        return f'Cuit: {self.cuit} \nNombre: {self.nombre}\nApellido: {self.apellido}\nContraseña: {self.password}'

class Controller:
    # Aquí podríamos utilizar una lista para simular la BD guardando unicamente el cuit
    # y verificar si el guía ya existe
    guias_registrados = ['12345678912', '98765432112']

    def validar_guia(self, cuit, nombre, apellido):
    # Verificamos que los datos ingresados sean válidos
        if self.validar_datos(cuit, nombre, apellido):
            # Pedimos una contraseña al guía
            interfaz = Interfaz()
            password = interfaz.pedir_contraseña()
            # Creamos un objeto Guia con los datos ingresados y la contraseña
            guia = Guia(cuit, nombre, apellido, password)
            #Agregamos CUIT del guia a la "bd"
            self.guias_registrados.append(guia.cuit)
            return guia
        else:
            return None
        
    def validar_datos(self, cuit, nombre, apellido):
        # Validamos el CUIT
        if self.validar_cuit(cuit) == False:
            interfaz = Interfaz()
            interfaz.mostrar_error("El CUIT ingresado no es válido.")
            return False
    
        # Validamos el nombre y el apellido
        if self.validar_nombre_apellido(nombre, apellido) == False:
            interfaz = Interfaz()
            interfaz.mostrar_error("El nombre y/o apellido ingresados no son válidos.")
            return False
    
        # Verificamos que los datos no estén en la BD
        for guia in self.guias_registrados:
            if guia == cuit:
                interfaz = Interfaz()
                interfaz.mostrar_error("Los datos del guía ya están registrados.")
                return False
        # Si todo está correcto, retornamos True
        else:
            return True
    
    def validar_cuit(self, cuit):
        # Validamos que el CUIT tenga un formato válido (11 dígitos)
        if not cuit.isdigit() or len(cuit) != 11:
            return False
        return True
    
    def validar_nombre_apellido(self, nombre, apellido):
        #Validamos que nombre y apellido no esten vacios
        if not nombre.isalpha() or not apellido.isalpha():
            return False
        return True

def main ():
    #instancia
    interfaz = Interfaz()

    cuit = interfaz.pedir_cuit()
    nombre = interfaz.pedir_nombre()
    apellido = interfaz.pedir_apellido()

    controller = Controller()

    guia = controller.validar_guia(cuit, nombre, apellido)

    if guia is not None:
        interfaz.mostrar_exito("Registro exitoso.")
        print(guia)
    else:
        interfaz.mostrar_error("Error en el registro.")


#Entrypoint->función o método que se debe llamar cuando se inicia una aplicación o paquete
if __name__ == '__main__':
    main()

#Aaaaa