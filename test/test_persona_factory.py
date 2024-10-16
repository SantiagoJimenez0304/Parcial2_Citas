import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))
import pytest
from app.persona_factory import PersonaFactory
from app.paciente import Paciente
from app.medico import Medico
from datetime import datetime

# Test para crear un paciente usando la fábrica
def test_crear_paciente():
    fecha_nacimiento = datetime(1990, 6, 15)
    paciente = PersonaFactory.crear_persona("paciente", 1, "Carlos", "Lopez", fecha_nacimiento, "Masculino", "Calle 45", "555-4321", "carlos@example.com")
    
    assert isinstance(paciente, Paciente)
    assert paciente.nombre == "Carlos"
    assert paciente.apellido == "Lopez"

# Test para crear un médico usando la fábrica
def test_crear_medico():
    fecha_nacimiento = datetime(1985, 5, 20)
    medico = PersonaFactory.crear_persona("medico", 2, "Ana", "Ramirez", fecha_nacimiento, "Femenino", "Calle 50", "555-5678", "ana@example.com", "Cardiología")
    
    assert isinstance(medico, Medico)
    assert medico.nombre == "Ana"
    assert medico.especialidad == "Cardiología"

# Test para manejar tipo de persona no válido
def test_tipo_persona_no_valido():
    with pytest.raises(ValueError) as excinfo:
        PersonaFactory.crear_persona("ingeniero", 3, "Luis", "Perez", datetime(1992, 7, 30), "Masculino", "Calle 60", "555-7890", "luis@example.com")
    
    assert str(excinfo.value) == "Tipo de persona 'ingeniero' no es reconocido"
