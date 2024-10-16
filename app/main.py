import csv
import json
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
from hospital import Hospital
from paciente import Paciente
from medico import Medico
from notificacion import NotificacionCorreo, NotificacionSMS, NotificacionWhatsapp
from reporte import Reporte

console = Console()

def cargar_datos_iniciales(hospital):
    console.print("[bold blue]Cargando datos iniciales...[/bold blue]")
    # Cargar pacientes desde CSV
    with open('datos//pacientes.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            paciente = Paciente(
                row['identificación'], row['nombre_completo'].split()[0], 
                ' '.join(row['nombre_completo'].split()[1:]),
                '1990-01-01', 'No especificado',
                'No especificada', row['celular'], row['correo']
            )
            hospital.agregar_paciente(paciente)
    console.print("[orange1]Pacientes cargados con éxito[/orange1]")

    # Cargar médicos desde JSON
    with open('datos/medicos.json', 'r', encoding='utf-8') as file:
        medicos_data = json.load(file)
        for medico_data in medicos_data:
            medico = Medico(
                medico_data['id'], medico_data['nombre'], medico_data['apellido'],
                medico_data['fecha_nacimiento'], medico_data['genero'],
                medico_data['direccion'], medico_data['telefono'],
                medico_data['email'], medico_data['especialidad']
            )
            hospital.agregar_medico(medico)
    console.print("[orange1]Médicos cargados con éxito[/orange1]")

    # Cargar citas desde CSV
    with open('datos/citas.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            paciente = hospital.buscar_paciente(row['paciente'])
            medico = hospital.buscar_medico(row['medicos'])
            if paciente and medico:
                fecha_hora = datetime.strptime(row['fecha_hora'], '%Y-%m-%d %H:%M:%S')
                hospital.agendar_cita(paciente, medico, fecha_hora.date(), fecha_hora.time())
    console.print("[orange1]Citas cargadas con éxito[/orange1]")

def mostrar_menu_principal():
    console.print(Panel("[bold orange1]Agendamiento de citas medicas[/bold orange1]", style="orange1"))
    table = Table(show_header=False, box=None, highlight=True)
    table.add_row("[bold orange1]1.[/bold orange1] Agendar una cita")
    table.add_row("[bold orange1]2.[/bold orange1] Cancelar una cita")
    table.add_row("[bold orange1]3.[/bold orange1] Mover una cita")
    table.add_row("[bold orange1]4.[/bold orange1] Ver las citas")
    table.add_row("[bold orange1]5.[/bold orange1] Generar un reporte de citas")
    table.add_row("[bold orange1]6.[/bold orange1] Salir del agendamiento")
    console.print(table)

def agendar_cita(hospital):
    console.print("[bold blue]Agendar nueva cita[/bold blue]")
    id_paciente = Prompt.ask("[red]ID del paciente[/red]")
    paciente = hospital.buscar_paciente(id_paciente)
    if not paciente:
        console.print("[bold red]Paciente no encontrado[/bold red]")
        return

    especialidad = Prompt.ask("[red]Especialidad requerida[/red]")
    medicos_disponibles = hospital.buscar_medicos_por_especialidad(especialidad)
    if not medicos_disponibles:
        console.print("[bold red]No hay médicos disponibles para esta especialidad[/bold red]")
        return

    console.print("[bold blue]los Médicos disponibles son:[/bold blue]")
    for i, medico in enumerate(medicos_disponibles, 1):
        console.print(f"[bold orange1]{i}. {medico.obtener_info()}[/bold orange1]")

    seleccion = int(Prompt.ask("[red]Seleccione un médico de preferencia (número)[/red]")) - 1
    medico = medicos_disponibles[seleccion]

    fecha = Prompt.ask("[red]Fecha de la cita (YYYY-MM-DD)[/red]")
    hora = Prompt.ask("[red]Hora de la cita (HH:MM)[/red]")

    if hospital.agendar_cita(paciente, medico, fecha, hora):
        console.print("[bold blue]Cita agendada con éxito[/bold blue]")
        notificacion = NotificacionCorreo(paciente.email, "Cita Agendada", f"Su cita con Dr. {medico.nombre} ha sido agendada para el {fecha} a las {hora}")
        notificacion.enviar_notificacion()
    else:
        console.print("[bold red]No se pudo agendar la cita[/bold red]")

def cancelar_cita(hospital):
    console.print("[bold red]Cancelar cita[/bold red]")
    citas = hospital.obtener_citas()
    if not citas:
        console.print("[bold red]No hay citas agendadas[/bold red]")
        return

    for i, cita in enumerate(citas, 1):
        console.print(f"[bold orange1]{i}. {cita}[/bold orange1]")

    seleccion = int(Prompt.ask("[red]Seleccione la cita a cancelar (número)[/red]")) - 1
    cita = citas[seleccion]

    if hospital.cancelar_cita(cita):
        console.print("[bold blue]Cita cancelada con éxito[/bold blue]")
        notificacion = NotificacionSMS(cita.paciente.telefono, f"Su cita del {cita.fecha} a las {cita.hora} ha sido cancelada")
        notificacion.enviar_notificacion()
    else:
        console.print("[bold red]No se pudo cancelar la cita[/bold red]")

def mover_cita(hospital):
    console.print("[bold orange1]Mover cita[/bold orange1]")
    citas = hospital.obtener_citas()
    if not citas:
        console.print("[bold red]No hay citas agendadas[/bold red]")
        return

    for i, cita in enumerate(citas, 1):
        console.print(f"[bold orange1]{i}. {cita}[/bold orange1]")

    seleccion = int(Prompt.ask("[red]Seleccione la cita a mover (número)[/red]")) - 1
    cita_original = citas[seleccion]

    nueva_fecha = Prompt.ask("[red]Nueva fecha (YYYY-MM-DD)[/red]")
    nueva_hora = Prompt.ask("[red]Nueva hora (HH:MM)[/red]")

    if hospital.mover_cita(cita_original, nueva_fecha, nueva_hora):
        console.print("[bold blue]Cita movida con éxito[/bold blue]")
        notificacion = NotificacionWhatsapp(cita_original.paciente.telefono, f"Su cita ha sido movida al {nueva_fecha} a las {nueva_hora}")
        notificacion.enviar_notificacion()
    else:
        console.print("[bold red]No se pudo mover la cita[/bold red]")

def ver_citas(hospital):
    console.print("[bold blue]Citas agendadas[/bold blue]")
    citas = hospital.obtener_citas()
    if not citas:
        console.print("[bold red]No hay citas agendadas[/bold red]")
        return

    table = Table(title="[bold orange1]Citas Agendadas[/bold orange1]", box=None, highlight=True)
    table.add_column("[bold blue]Paciente[/bold blue]", style="blue")
    table.add_column("[bold red]Médico[/bold red]", style="red")
    table.add_column("[bold orange1]Fecha[/bold orange1]", style="orange1")
    table.add_column("[bold blue]Hora[/bold blue]", style="blue")

    for cita in citas:
        table.add_row(
            f"[bold blue]{cita.paciente.nombre} {cita.paciente.apellido}[/bold blue]",
            f"[bold red]Dr. {cita.medico.nombre} {cita.medico.apellido}[/bold red]",
            f"[bold orange1]{cita.fecha}[/bold orange1]",
            f"[bold blue]{cita.hora}[/bold blue]"
        )

    console.print(table)

def generar_reporte_citas(hospital):
    citas = hospital.obtener_citas()
    Reporte.generar_reporte_citas(citas)

def main():
    hospital = Hospital("Hospital Central")
    cargar_datos_iniciales(hospital)

    while True:
        mostrar_menu_principal()
        opcion = Prompt.ask("[red]Seleccione una opción para continuar[/red]", choices=["1", "2", "3", "4", "5", "6"])

        if opcion == "1":
            agendar_cita(hospital)
        elif opcion == "2":
            cancelar_cita(hospital)
        elif opcion == "3":
            mover_cita(hospital)
        elif opcion == "4":
            ver_citas(hospital)
        elif opcion == "5":
            generar_reporte_citas(hospital)
        elif opcion == "6":
            console.print("[bold orange1]Saliendo del sistema. ¡Hasta luego![/bold orange1]")
            break

if __name__ == "__main__":
    main()