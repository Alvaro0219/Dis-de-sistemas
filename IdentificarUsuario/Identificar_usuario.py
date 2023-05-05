
class Cliente:
    def __init__(self, correo, nombre, apellido, dni, cuit, domicilio, telefono, ciudad, pais, contraseña):
        self.correo = correo
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.cuit = cuit
        self.domicilio = domicilio
        self.telefono = telefono
        self.ciudad = ciudad
        self.pais = pais
        self.contraseña = contraseña

class Controller:
    def __init__(self):
        #Diccionario: Clave->Email Valor->Objeto de tipo Cliente
        self.clientes = {
            "cliente1@gmail.com": Cliente("cliente1@gmail.com", "Juan", "Perez", "12345678", "11111111111", "Calle 1", "555-5555", "Provincia 1", "Argentina", "contraseña1"),
            "cliente2@gmail.com": Cliente("cliente2@gmail.com", "Ana", "Gomez", "87654321", "22222222222", "Calle 2", "555-5555", "Provincia 2", "Argentina", "contraseña2"),
            "cliente3@gmail.com": Cliente("cliente3@gmail.com", "Pedro", "Rodriguez", "13579246", "33333333333", "Calle 3", "555-5555", "Provincia 3", "Argentina", "contraseña3")
        }

    def verificar_correo(self, correo):
        return correo in self.clientes

    def verificar_contraseña(self, correo, contraseña):
        #si la contraseña proporcionada por el usuario coincide con la contraseña almacenada en el diccionario de clientes para ese correo.
        return correo in self.clientes and self.clientes[correo].contraseña == contraseña

class Interfaz:
    def __init__(self):
        self.controller = Controller()

    def menu(self, correo):
        cliente = self.controller.clientes[correo]
        print(f"Bienvenido al menú de la app {cliente.nombre} {cliente.apellido}")

def main():
    interfaz = Interfaz()
    correo = input("Ingrese su correo: ")
    while not interfaz.controller.verificar_correo(correo):
        print("Correo no registrado, ingrese otro")
        correo = input("Ingrese su correo: ")
    contraseña = input("Ingrese su contraseña: ")
    while not interfaz.controller.verificar_contraseña(correo, contraseña):
        print("Contraseña incorrecta, ingrese otra")
        contraseña = input("Ingrese su contraseña: ")
    
    # Redirigir el usuario al menu luego de que ingrese los datos correctamente
    interfaz.menu(correo)

if __name__ == "__main__":
    main()