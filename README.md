Sistema de Gestión de Citas Médicas
Descripción
Este sistema permite la gestión de citas médicas, incluyendo la posibilidad de agendar, cancelar, mover y ver citas, así como generar reportes de las mismas. El sistema usa la biblioteca rich para la presentación de datos de manera estética en la consola.

Requisitos
Para ejecutar este sistema, necesitas instalar las dependencias siguientes. Asegúrate de tener Python 3.6 o superior instalado.

Requisitos del sistema
txt
Copiar código
rich==13.0.1
Instalación de dependencias
Para instalar las dependencias necesarias, ejecuta:

bash
Copiar código
pip install -r requirements.txt
Clases Utilizadas
1. Persona (abstracta)
Descripción: Clase base abstracta para representar a cualquier persona (paciente o médico) con los atributos básicos como id, nombre, apellido, fecha_nacimiento, genero, direccion, telefono y email.
Método: obtener_info(): Método abstracto que cada clase hija debe implementar para mostrar la información de la persona.
2. Paciente
Descripción: Representa a un paciente. Hereda de la clase Persona e incluye un historial médico (historial_medico).
Métodos:
agregar_historial(): Agrega una entrada al historial médico.
obtener_historial(): Devuelve el historial médico del paciente.
obtener_info(): Devuelve una cadena con la información del paciente.
3. Medico
Descripción: Representa a un médico. Hereda de la clase Persona e incluye una especialidad médica.
Métodos:
obtener_info(): Devuelve una cadena con la información del médico.
4. Cita
Descripción: Representa una cita médica que incluye a un paciente, un médico, la fecha y la hora de la cita.
Métodos:
__str__(): Representación en cadena de la cita, incluyendo la información del paciente, médico, fecha y hora.
5. Hospital
Descripción: La clase principal para manejar la lógica del sistema, que incluye la gestión de pacientes, médicos y citas.
Métodos:
agregar_paciente(): Agrega un paciente al hospital.
agregar_medico(): Agrega un médico al hospital.
agendar_cita(): Agenda una nueva cita para un paciente con un médico.
cancelar_cita(): Cancela una cita existente.
mover_cita(): Mueve una cita a una nueva fecha y hora.
obtener_citas(): Devuelve todas las citas agendadas.
6. Notificaciones
Descripción: Clases para enviar notificaciones a los pacientes sobre el estado de sus citas, como confirmaciones de citas, cancelaciones y cambios de horario. Se manejan por medio de las siguientes clases:
NotificacionCorreo: Envía un correo electrónico.
NotificacionSMS: Envía un mensaje SMS.
NotificacionWhatsapp: Envía un mensaje de WhatsApp.
7. Reporte
Descripción: Clase para generar reportes de citas médicas.
Métodos:
generar_reporte_citas(): Muestra un reporte de todas las citas médicas agendadas en formato de tabla.
Ejecución del programa
Para ejecutar el programa, simplemente corre el archivo main.py en tu terminal o consola:

bash
Copiar código
python main.py
El programa cargará los datos iniciales desde los archivos CSV y JSON (ubicados en la carpeta datos/), y luego te mostrará un menú interactivo para gestionar las citas médicas.

Menú del sistema
El menú te permitirá elegir entre las siguientes opciones:

Agendar una nueva cita.
Cancelar una cita existente.
Mover una cita a una nueva fecha y hora.
Ver las citas agendadas.
Generar un reporte de citas.
Salir del sistema.
Archivos de datos
El sistema carga datos iniciales desde los siguientes archivos:

Pacientes: datos/pacientes.csv
Médicos: datos/medicos.json
Citas: datos/citas.csv
Asegúrate de que estos archivos existan en el directorio datos/ antes de ejecutar el programa. Si deseas cargar tus propios datos, simplemente sigue el formato de los archivos existentes.
