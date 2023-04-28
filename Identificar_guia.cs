using System.Net.Mail;

UI.IdentificarGuia();

class UI
{
    static internal void IdentificarGuia()
    {
        Console.WriteLine("Ingrese su correo electrónico");
        var email = Console.ReadLine();

        try
        {
            new MailAddress(email);
        }
        catch (FormatException)
        {
            Console.WriteLine("Correo inválido");
            return;
        }

        var controller = new Controller();
        var correoExiste = controller.VerificarCorreoElectronico(email);

        if (!correoExiste)
        {
            Console.WriteLine("Correo no reconocido");
            return;
        }

        Console.WriteLine("Ingrese su contraseña");
        var password = Console.ReadLine();

        var passwordOk = controller.VerificarContraseña(email, password);
        if (!passwordOk)
        {
            Console.WriteLine("Contraseña incorrecta");
            return;
        }

        Console.WriteLine("Bienvenido");
    }
}

class Controller
{
    internal bool VerificarCorreoElectronico(string correo) => 
        new Persistencia().VerificarCorreoElectronico(correo);

    internal bool VerificarContraseña(string correo, string passwordProvista)
    {
        var persistencia = new Persistencia();
        var passwordAlmaceda = persistencia.BuscarContraseña(correo);

        if (passwordAlmaceda == null)
        {
            return false;
        }

        return passwordProvista == passwordAlmaceda;
    }
}
class Persistencia
{
    static List<Guia> Guias = new()
    {
        new Guia
        { CorreoElectronico = "jp@example.com", Contraseña = "123456" }
    };

    internal bool VerificarCorreoElectronico(string correo)
    {
        return Guias.Any(guia => guia.CorreoElectronico == correo);
    }

    internal string BuscarContraseña(string correo)
    {
        var guia = Guias.Find(guia => guia.CorreoElectronico == correo);

        if (guia == null)
        {
            return null;
        }
        else
        {
            return guia.Contraseña;
        }
    }


}

class Guia
{
    public string CorreoElectronico { get; set; }
    public string Contraseña { get; set; }
}