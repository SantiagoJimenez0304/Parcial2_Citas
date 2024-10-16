import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))
import pytest
from app.medico import Medico
from datetime import datetime

# Prueba para verificar la correcta creación de un objeto Medico
def test_creacion_medico():
    fecha_nacimiento = datetime(1980, 5, 15)
    medico = Medico(1, "Sofia", "Gomez", fecha_nacimiento, "Femenino", "Calle 123", "555-1234", "sofia@gmail.com", "Cardiología")
    
    assert medico.id == 1
    assert medico.nombre == "Sofia"
    assert medico.apellido == "Gomez"
    assert medico.fecha_nacimiento == fecha_nacimiento
    assert medico.genero == "Femenino"
    assert medico.direccion == "Calle 123"
    assert medico.telefono == "555-1234"
    assert medico.email == "sofia@gmail.com"
    assert medico.especialidad == "Cardiología"

# Prueba para el método obtener_info()
def test_obtener_info():
    fecha_nacimiento = datetime(1980, 5, 15)
    medico = Medico(1, "Sofia", "Gomez", fecha_nacimiento, "Femenino", "Calle 123", "555-1234", "sofia@gmail.com", "Cardiología")
    
    info = medico.obtener_info()
    assert info == "Dr. Sofia Gomez, Especialidad: Cardiología, ID: 1"
