from rich.console import Console
from rich.table import Table

class Reporte:
    @staticmethod
    def generar_reporte_citas(citas):
        mi_consola = Console()
        mi_tabla = Table(title="Listado de Citas Médicas")
        
        mi_tabla.add_column("Paciente", style="cyan")
        mi_tabla.add_column("Médico", style="magenta")
        mi_tabla.add_column("Fecha", style="green")
        mi_tabla.add_column("Hora", style="yellow")
        
        for cita in citas:
            paciente_info = f"{cita.paciente.nombre} {cita.paciente.apellido}"
            medico_info = f"Dr. {cita.medico.nombre} {cita.medico.apellido}"
            fecha_cita = str(cita.fecha)
            hora_cita = str(cita.hora)
            
            mi_tabla.add_row(paciente_info, medico_info, fecha_cita, hora_cita)
        
        mi_consola.print(mi_tabla)
