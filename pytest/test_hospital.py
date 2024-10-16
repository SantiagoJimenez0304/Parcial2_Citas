import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))
from datetime import datetime, timedelta
from app.hospital import Hospital
from app.cita import Cita
from app.agenda import Agenda

# Clases simuladas para Paciente y Medico
class Paciente:
    def __init__(self, id, nombre, apellido):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido

class Medico:
    def __init__(self, id, nombre, apellido, especialidad):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad

# Prueba para agregar un paciente al hospital
def test_agregar_paciente():
    hospital = Hospital("Hospital General")
    paciente = Paciente(1, "Juan", "Perez")
    
    hospital.agregar_paciente(paciente)
    
    assert len(hospital.pacientes) == 1
    assert hospital.pacientes[0] == paciente

# Prueba para agregar un médico al hospital
def test_agregar_medico():
    hospital = Hospital("Hospital General")
    medico = Medico(1, "Sofia", "Gomez", "Cardiología")
    
    hospital.agregar_medico(medico)
    
    assert len(hospital.medicos) == 1
    assert hospital.medicos[0] == medico

# Prueba para buscar un paciente por ID
def test_buscar_paciente():
    hospital = Hospital("Hospital General")
    paciente = Paciente(1, "Juan", "Perez")
    
    hospital.agregar_paciente(paciente)
    resultado = hospital.buscar_paciente(1)
    
    assert resultado == paciente

# Prueba para buscar un médico por ID
def test_buscar_medico():
    hospital = Hospital("Hospital General")
    medico = Medico(1, "Sofia", "Gomez", "Cardiología")
    
    hospital.agregar_medico(medico)
    resultado = hospital.buscar_medico(1)
    
    assert resultado == medico

# Prueba para agendar una cita
def test_agendar_cita():
    hospital = Hospital("Hospital General")
    paciente = Paciente(1, "Juan", "Perez")
    medico = Medico(1, "Sofia", "Gomez", "Cardiología")
    fecha = datetime.now()
    hora = "10:00"
    
    hospital.agregar_paciente(paciente)
    hospital.agregar_medico(medico)
    
    resultado = hospital.agendar_cita(paciente, medico, fecha, hora)
    assert resultado == True
    assert len(hospital.obtener_citas()) == 1

# Prueba para cancelar una cita
def test_cancelar_cita():
    hospital = Hospital("Hospital General")
    paciente = Paciente(1, "Juan", "Perez")
    medico = Medico(1, "Sofia", "Gomez", "Cardiología")
    fecha = datetime.now()
    hora = "10:00"
    
    hospital.agregar_paciente(paciente)
    hospital.agregar_medico(medico)
    
    cita = Cita(paciente, medico, fecha, hora)
    hospital.agendar_cita(paciente, medico, fecha, hora)
    assert hospital.cancelar_cita(cita) == True
    assert len(hospital.obtener_citas()) == 0

# Prueba para mover una cita a otra fecha/hora
def test_mover_cita():
    hospital = Hospital("Hospital General")
    paciente = Paciente(1, "Juan", "Perez")
    medico = Medico(1, "Sofia", "Gomez", "Cardiología")
    fecha = datetime.now()
    nueva_fecha = fecha + timedelta(days=1)
    hora = "10:00"
    nueva_hora = "11:00"
    
    hospital.agregar_paciente(paciente)
    hospital.agregar_medico(medico)
    
    cita = Cita(paciente, medico, fecha, hora)
    hospital.agendar_cita(paciente, medico, fecha, hora)
    assert hospital.mover_cita(cita, nueva_fecha, nueva_hora) == True
    cita_moved = hospital.obtener_citas()[0]
    assert cita_moved.fecha == nueva_fecha
    assert cita_moved.hora == nueva_hora

# Prueba para buscar médicos por especialidad
def test_buscar_medicos_por_especialidad():
    hospital = Hospital("Hospital General")
    medico1 = Medico(1, "Sofia", "Gomez", "Cardiología")
    medico2 = Medico(2, "Carlos", "Rodriguez", "Neurología")
    
    hospital.agregar_medico(medico1)
    hospital.agregar_medico(medico2)
    
    cardiologos = hospital.buscar_medicos_por_especialidad("Cardiología")
    assert len(cardiologos) == 1
    assert cardiologos[0] == medico1
