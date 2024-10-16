import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))
import pytest
from datetime import datetime
from app.paciente import Paciente

# Test para verificar la correcta creación de un objeto Paciente
def test_creacion_paciente():
    fecha_nacimiento = datetime(1990, 6, 15)
    paciente = Paciente(1, "Carlos", "Lopez", fecha_nacimiento, "Masculino", "Calle 45", "555-4321", "carlos@example.com")
    
    assert paciente.id == 1
    assert paciente.nombre == "Carlos"
    assert paciente.apellido == "Lopez"
    assert paciente.fecha_nacimiento == fecha_nacimiento
    assert paciente.genero == "Masculino"
    assert paciente.direccion == "Calle 45"
    assert paciente.telefono == "555-4321"
    assert paciente.email == "carlos@example.com"
    assert paciente.historial_medico == []

# Test para agregar y obtener historial médico
def test_agregar_obtener_historial():
    fecha_nacimiento = datetime(1990, 6, 15)
    paciente = Paciente(1, "Carlos", "Lopez", fecha_nacimiento, "Masculino", "Calle 45", "555-4321", "carlos@example.com")
    
    entrada_historial = "Consulta por fiebre alta"
    paciente.agregar_historial(entrada_historial)
    
    historial = paciente.obtener_historial()
    
    assert len(historial) == 1
    assert historial[0] == entrada_historial

# Test para obtener información del paciente
def test_obtener_info():
    fecha_nacimiento = datetime(1990, 6, 15)
    paciente = Paciente(1, "Carlos", "Lopez", fecha_nacimiento, "Masculino", "Calle 45", "555-4321", "carlos@example.com")
    
    info = paciente.obtener_info()
    
    assert info == "Paciente: Carlos Lopez, ID: 1"
