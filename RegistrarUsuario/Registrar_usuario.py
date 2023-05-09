import re

#Clase que representa a un usuario registrado en el sistema.
class Usuario:
    def __init__(self, email, nombre, apellido, dni, cuit, domicilio, telefono, ciudad, pais, contrasena):
        self.email = email
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.cuit = cuit
        self.domicilio = domicilio
        self.telefono = telefono
        self.ciudad = ciudad
        self.pais = pais
        self.contrasena = contrasena

"""
    Clase que define la interfaz de usuario del sistema.

    Métodos:
    - obtener_datos_usuario(): solicita al usuario que ingrese sus datos personales y retorna un objeto Usuario con dichos datos.
"""
class Interfaz:
    # Método que se puede llamar directamente en la clase, sin necesidad de crear una instancia de la clase.
    @staticmethod
    def obtener_datos_usuario():
        while True:
            email = input("Ingrese su email: ")
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                print("Por favor, ingrese una dirección de correo electrónico válida.")
                continue
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            dni = input("Ingrese su DNI: ")
            cuit = input("Ingrese su CUIT: ")
            domicilio = input("Ingrese su domicilio: ")
            telefono = input("Ingrese su teléfono: ")
            ciudad = input("Ingrese su ciudad: ")
            pais = input("Ingrese su país: ")
            while True:
                contrasena = input("Ingrese su contraseña: ")
                if not contrasena or len(contrasena) < 8:
                    print("Por favor, ingrese una contraseña de al menos 8 caracteres.")
                else:
                    break
            return Usuario(email, nombre, apellido, dni, cuit, domicilio, telefono, ciudad, pais, contrasena)
"""
    Clase que define la lógica de negocio del sistema.

    Atributos:
    - usuarios (dict): diccionario que almacena a los usuarios registrados en el sistema. Las claves son los correos electrónicos de los usuarios, y los valores son objetos Usuario.

    Métodos:
    - validar_usuario(usuario: Usuario) -> bool: valida que los datos ingresados por el usuario sean correctos y no exista un usuario registrado con el mismo correo electrónico.
    - registrar_usuario(usuario: Usuario) -> None: registra un nuevo usuario en el sistema si los datos ingresados son correctos.
    """
class Controller:
    def __init__(self):
        #BD
        self.usuarios = {"cliente1@gmail.com": Usuario("cliente1@gmail.com", "Juan", "Perez", "12345678", "11111111111", "Calle 1", "555-5555", "Provincia 1", "Argentina", "contraseña1")}

    def validar_usuario(self, usuario):
        #Verificamos que el usuario no este en la BD
        if usuario.email in self.usuarios:
            print("\n-------------------------------------")
            print("El usuario ya está registrado. Por favor, ingrese un correo electrónico diferente.")
            return False
        #Verificamos que no haya ningun campo vacio
        if any(not getattr(usuario, atributo) for atributo in ["nombre", "apellido", "dni", "cuit", "domicilio", "telefono", "ciudad", "pais"]):
            print("\n-------------------------------------")
            print("Por favor, complete todos los campos.")
            return False
    
        return True
    
    def registrar_usuario(self, usuario):
        if self.validar_usuario(usuario):
            self.usuarios[usuario.email] = usuario
            print("\n-------------------------------------")
            print("Registro exitoso. Por favor, inicie sesión con sus credenciales.")
            print(f"Email: {usuario.email}")
            print(f"Contraseña: {usuario.contrasena}")
            print("-------------------------------------")
        else:
            print("Error al registrar el usuario. Por favor, intente nuevamente.")
            print("-------------------------------------")
            

"""
    Punto de entrada del programa. Muestra un menú de opciones al usuario y ejecuta la opción seleccionada.
"""
def main():
    #instancias
    controller = Controller()
    interfaz = Interfaz()
    
    while True:
        print("Bienvenido al sistema de registro. Por favor, seleccione una opción:")
        print("1. Registrar un nuevo usuario")
        print("2. Salir")
        
        opcion = input("Opción seleccionada: ")
        
        if opcion == "1":
            usuario = interfaz.obtener_datos_usuario()
            controller.registrar_usuario(usuario)
        elif opcion == "2":
            print("Gracias por utilizar nuestro sistema de registro.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
