<h1>TURNERO</h1>

<h2>REQUERIMIENTOS FUNCIONALES</h2>
*REGISTRO DE TURNOS -> El sistema debe permitir a los usuarios registrar nuevos turnos, pidiendo su DNI como dato unico.
<br>
*VISUALIZACION DE TURNOS -> El sistema debe mostrar en una pantalla visible los turnos programados con una diferencia entre los que se atendieron, el actual y los que siguen.
<br>
*ATENCION DE TURNOS -> El sistema debe permitir al personal del box tomar los turnos para su correspondiente atención respetando el orden de llegada 
<br>
*PRIORIZACION DE TURNOS -> El sistema debe perimitir al personal del box marcar ciertos turnos como 'prioritarios'
<br>

<h2>REQUERIMIENTOS NO FUNCIONALES</h2>
*USABILIDAD -> El sistema debe ser intuitivo y facil de usar dado que mucha gente de mayor edad dispondra del mismo
<br>
*DESEMPEÑO -> El sistema debe ser capaz de manejar una gran carga de usuarios y turnos


<h2>FLUJO DE FUNCIONAMIENTO</h2>
USUARIO
1 -> EL paciente accede a la UI dispuesta en una tablet para tomar un turno (consulta con el box) o para visualizar los turnos a su nombre
<br>
2 -> El sistema emite un ticket al paciente con el codigo de turno y el nro de box
<br>
3 -> El sistema muestra en una UI visible los turnos, mostrando: numero de box, codigo de turno y apellido del paciente
<br>
PERSONAL DEL BOX
1 -> El sistema debe brindarle al personal una lista de todos los turnos en espera segun orden de llegada
<br>
2 -> El personal elige un turno segun orden de llegada o puede atender un turno en especifico 
<br>
2.1 -> Si el paciente tiene turno el sistema debe mostrar los detalles del mismo para que el personal rediriga al paciente
<br>
2.2 -> Si el paciente no tiene turno el sistema debe permitir generar un nuevo turno

<h2>DESCRIPCION DE ARQUITECTURA</h2>
![image](https://github.com/Alvaro0219/Dis-de-sistemas/assets/112023160/1d8efd99-ef31-4d66-8e0f-45d33607668e)
