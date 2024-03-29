<h1>TURNERO</h1>

<h2>REQUERIMIENTOS FUNCIONALES</h2>
<h3>REGISTRO DE TURNOS</h3> -> El sistema debe permitir a los usuarios registrar nuevos turnos, pidiendo su DNI como dato unico.
<br>
<h3>VISUALIZACION DE TURNOS</h3> -> El sistema debe mostrar en una pantalla visible los turnos programados con una diferencia entre los que se atendieron, el actual y los que siguen.
<br>
<h3>ATENCION DE TURNOS</h3> -> El sistema debe permitir al personal del box tomar los turnos para su correspondiente atención respetando el orden de llegada 
<br>
*PRIORIZACION DE TURNOS</h3> -> El sistema debe perimitir al personal del box marcar ciertos turnos como 'prioritarios'
<br>

<h2>REQUERIMIENTOS NO FUNCIONALES</h2>
<h3>USABILIDAD</h3> -> El sistema debe ser intuitivo y facil de usar dado que mucha gente de mayor edad dispondra del mismo
<br>
<h3>DESEMPEÑO</h3> -> El sistema debe ser capaz de manejar una gran carga de usuarios y turnos


<h2>FLUJO DE FUNCIONAMIENTO</h2>
<h3>USUARIO</h3>
1 -> EL paciente accede a la UI dispuesta en una tablet para tomar un turno (consulta con el box) o para visualizar los turnos a su nombre
<br>
2 -> Si el paciente decide registrar un turno el sistema emite un ticket al paciente con el codigo de turno y el nro de box para que en el mismo le tomen los datos
<br>
3 -> El sistema muestra en una UI visible los turnos, mostrando: numero de box, codigo de turno y apellido del paciente
<br>
<h3>PERSONAL DEL BOX</h3>
1 -> El sistema debe brindarle al personal una lista de todos los turnos en espera segun orden de llegada
<br>
2 -> El personal elige un turno segun orden de llegada o puede atender un turno en especifico 
<br>
2.1 -> Si el paciente tiene turno el sistema debe mostrar los detalles del mismo para que el personal rediriga al paciente
<br>
2.2 -> Si el paciente no tiene turno el sistema debe permitir generar un nuevo turno

<h2>DESCRIPCION DE ARQUITECTURA</h2>
![image](https://github.com/Alvaro0219/Dis-de-sistemas/assets/112023160/1d8efd99-ef31-4d66-8e0f-45d33607668e)
<br>
Para el sistema de gestion de turnos elegimos un tipo de arquitectura en capas ya que la misma nos ofrece claridad, mantenibilidad, escalabilidad, flexibilidad,  y control .
