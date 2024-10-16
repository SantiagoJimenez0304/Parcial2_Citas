from paciente import Paciente
from medico import Medico

class PersonaFactory:
    @staticmethod
    def crear_persona(tipo, *args):
        tipos = {
            "paciente": Paciente,
            "medico": Medico
        }
        
        if tipo in tipos:
            return tipos[tipo](*args)
        else:
            raise ValueError(f"Tipo de persona '{tipo}' no es reconocido")
