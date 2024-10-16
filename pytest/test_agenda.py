import sys
import os

# Agrega la carpeta 'app' al sys.path para que Python la reconozca como un paquete
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))
import pytest
from datetime import datetime, timedelta
from app.cita import Cita
from app.agenda import Agenda

# Prueba para agendar una cita correctamente
def test_agendar_cita():
    agenda = Agenda()
    cita = Cita("Paciente 1", "Medico 1", datetime.now(), "10:00")
    
    assert agenda.agendar_cita(cita) == True
    assert len(agenda.obtener_citas()) == 1

# Prueba para verificar disponibilidad de una cita
def test_verificar_disponibilidad():
    agenda = Agenda()
    cita1 = Cita("Paciente 1", "Medico 1", datetime.now(), "10:00")
    cita2 = Cita("Paciente 2", "Medico 1", datetime.now(), "10:00")
    
    agenda.agendar_cita(cita1)
    assert agenda.verificar_disponibilidad(cita2) == False

# Prueba para cancelar una cita existente
def test_cancelar_cita():
    agenda = Agenda()
    cita = Cita("Paciente 1", "Medico 1", datetime.now(), "10:00")
    
    agenda.agendar_cita(cita)
    assert agenda.cancelar_cita(cita) == True
    assert len(agenda.obtener_citas()) == 0

# Prueba para mover una cita a una nueva fecha/hora
def test_mover_cita():
    agenda = Agenda()
    fecha_original = datetime.now()
    nueva_fecha = fecha_original + timedelta(days=1)
    
    cita = Cita("Paciente 1", "Medico 1", fecha_original, "10:00")
    agenda.agendar_cita(cita)
    
    assert agenda.mover_cita(cita, nueva_fecha, "11:00") == True
    assert len(agenda.obtener_citas()) == 1
    nueva_cita = agenda.obtener_citas()[0]
    
    assert nueva_cita.fecha == nueva_fecha
    assert nueva_cita.hora == "11:00"

# Prueba para mover una cita a una hora ya ocupada (debe fallar)
def test_mover_cita_hora_ocupada():
    agenda = Agenda()
    fecha = datetime.now()
    
    cita1 = Cita("Paciente 1", "Medico 1", fecha, "10:00")
    cita2 = Cita("Paciente 2", "Medico 1", fecha, "11:00")
    
    agenda.agendar_cita(cita1)
    agenda.agendar_cita(cita2)
    
    assert agenda.mover_cita(cita1, fecha, "11:00") == False
