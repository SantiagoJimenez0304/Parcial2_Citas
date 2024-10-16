import sys
import os

# Agrega la carpeta 'app' al sys.path para que Python la reconozca como un paquete
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))
from datetime import datetime
from app.cita import Cita

# Clases simuladas para Paciente y Medico
class Paciente:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Medico:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

# Prueba de creación de la cita
def test_crear_cita():
    paciente = Paciente("Juan", "Perez")
    medico = Medico("Sofia", "Gomez")
    fecha = datetime.now()
    hora = "10:00"
    
    cita = Cita(paciente, medico, fecha, hora)
    
    assert cita.paciente == paciente
    assert cita.medico == medico
    assert cita.fecha == fecha
    assert cita.hora == hora

# Prueba del método __str__
def test_cita_str():
    paciente = Paciente("Maria", "Lopez")
    medico = Medico("Carlos", "Rodriguez")
    fecha = datetime(2024, 10, 15)
    hora = "14:30"
    
    cita = Cita(paciente, medico, fecha, hora)
    
    resultado_esperado = "Cita: Maria Lopez con Dr. Carlos Rodriguez el 2024-10-15 00:00:00 a las 14:30"
    assert str(cita) == resultado_esperado
