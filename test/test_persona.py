import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))
import pytest
from app.persona import Persona
from datetime import datetime

# Crear una subclase de Persona para realizar la prueba
class PersonaConcreta(Persona):
    def obtener_info(self):
        return f"{self.nombre} {self.apellido}, ID: {self.id}"

# Test para verificar que la clase abstracta no puede ser instanciada directamente
def test_instanciar_clase_abstracta():
    with pytest.raises(TypeError) as excinfo:
        Persona(1, "Carlos", "Lopez", datetime(1990, 6, 15), "Masculino", "Calle 45", "555-4321", "carlos@example.com")
    
    assert "Can't instantiate abstract class Persona" in str(excinfo.value)

# Test para verificar que una subclase concreta puede ser instanciada y el método abstracto es implementado
def test_instanciar_subclase():
    fecha_nacimiento = datetime(1990, 6, 15)
    persona = PersonaConcreta(1, "Carlos", "Lopez", fecha_nacimiento, "Masculino", "Calle 45", "555-4321", "carlos@example.com")
    
    assert persona.nombre == "Carlos"
    assert persona.obtener_info() == "Carlos Lopez, ID: 1"
