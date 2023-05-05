class Cliente:
    def __init__(self, nombre, apellido, dni, cuit, domicilio, telefono, ciudad, pais, correo, contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.cuit = cuit
        self.domicilio = domicilio
        self.telefono = telefono
        self.ciudad = ciudad
        self.pais = pais
        self.correo = correo
        self.contraseña = contraseña

class Interfaz:
    def __init__(self):
        self.clientes = {
            "cliente1@gmail.com": "contraseña1",
            "cliente2@gmail.com": "contraseña2",
            "cliente3@gmail.com": "contraseña3"
        }

    def verificar_correo(self, correo):
        if correo in self.clientes:
            return True
        else:
            return False

    def verificar_contraseña(self, correo, contraseña):
        if self.clientes[correo] == contraseña:
            return True
        else:
            return False

    def registrar_cliente(self):
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        dni = input("Ingrese su DNI: ")
        cuit = input("Ingrese su CUIT: ")
        domicilio = input("Ingrese su domicilio: ")
        telefono = input("Ingrese su telefono: ")
        ciudad = input("Ingrese su ciudad: ")
        pais = input("Ingrese su pais: ")
        correo = input("Ingrese su correo: ")
        while self.verificar_correo(correo):
            print("Correo ya registrado, ingrese otro")
            correo = input("Ingrese su correo: ")
        contraseña = input("Ingrese su contraseña: ")
        cliente = Cliente(nombre, apellido, dni, cuit, domicilio, telefono, ciudad, pais, correo, contraseña)
        self.clientes[correo] = contraseña
        print("Cliente registrado exitosamente")

def main():
    interfaz = Interfaz()
    correo = input("Ingrese su correo: ")
    while not interfaz.verificar_correo(correo):
        print("Correo no registrado, ingrese otro")
        correo = input("Ingrese su correo: ")
    contraseña = input("Ingrese su contraseña: ")
    while not interfaz.verificar_contraseña(correo, contraseña):
        print("Contraseña incorrecta, ingrese otra")
        contraseña = input("Ingrese su contraseña: ")
    print("Bienvenido!")

if __name__ == "__main__":
    main()