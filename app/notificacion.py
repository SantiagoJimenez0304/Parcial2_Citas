from abc import ABC, abstractmethod

class Notificacion(ABC):
    @abstractmethod
    def enviar_notificacion(self):
        raise NotImplementedError("Este método debe ser implementado por una subclase")

class NotificacionCorreo(Notificacion):
    def __init__(self, destinatario, asunto, mensaje):
        self.destinatario = destinatario
        self.asunto = asunto
        self.mensaje = mensaje
    
    def enviar_notificacion(self):
        self._enviar_correo()

    def _enviar_correo(self):
        print(f"Enviando correo a: {self.destinatario}")
        print(f"Asunto: {self.asunto}")
        print(f"Mensaje: {self.mensaje}")

class NotificacionSMS(Notificacion):
    def __init__(self, numero, mensaje):
        self.numero = numero
        self.mensaje = mensaje
    
    def enviar_notificacion(self):
        self._enviar_sms()

    def _enviar_sms(self):
        print(f"Enviando SMS a: {self.numero}")
        print(f"Mensaje: {self.mensaje}")

class NotificacionWhatsapp(Notificacion):
    def __init__(self, numero, mensaje):
        self.numero = numero
        self.mensaje = mensaje
    
    def enviar_notificacion(self):
        self._enviar_whatsapp()

    def _enviar_whatsapp(self):
        print(f"Enviando WhatsApp a: {self.numero}")
        print(f"Mensaje: {self.mensaje}")
