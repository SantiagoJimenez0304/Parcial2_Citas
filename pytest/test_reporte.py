import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))
import pytest
from datetime import datetime
from rich.console import Console
from rich.table import Table
from app.cita import Cita
from app.paciente import Paciente
from app.medico import Medico
from app.reporte import Reporte

# Test para la clase Reporte
def test_generar_reporte_citas(capsys):
    # Crear datos de prueba
    paciente1 = Paciente(1, "Juan", "Perez", datetime(1990, 6, 15), "Masculino", "Calle 123", "555-1234", "juan@example.com")
    medico1 = Medico(1, "Carlos", "Ramirez", datetime(1985, 5, 20), "Masculino", "Avenida 45", "555-5678", "carlos@example.com", "Cardiología")
    cita1 = Cita(paciente1, medico1, datetime(2024, 10, 20), "10:00 AM")
    
    paciente2 = Paciente(2, "Maria", "Lopez", datetime(1992, 8, 5), "Femenino", "Calle 456", "555-9876", "maria@example.com")
    medico2 = Medico(2, "Ana", "Martinez", datetime(1978, 11, 2), "Femenino", "Avenida 78", "555-8765", "ana@example.com", "Dermatología")
    cita2 = Cita(paciente2, medico2, datetime(2024, 10, 21), "11:00 AM")
    
    citas = [cita1, cita2]
    
    # Generar el reporte
    Reporte.generar_reporte_citas(citas)
    
    # Capturar la salida de consola
    captured = capsys.readouterr()
    
    # Comprobar que se generó la tabla y que contiene las citas correctas
    assert "Listado de Citas Médicas" in captured.out
    assert "Juan Perez" in captured.out
    assert "Dr. Carlos Ramirez" in captured.out
    assert "2024-10-20" in captured.out
    assert "10:00 AM" in captured.out
    
    assert "Maria Lopez" in captured.out
    assert "Dr. Ana Martinez" in captured.out
    assert "2024-10-21" in captured.out
    assert "11:00 AM" in captured.out
