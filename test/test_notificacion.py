import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))
import pytest
from app.notificacion import NotificacionCorreo, NotificacionSMS, NotificacionWhatsapp

# Test para NotificacionCorreo
def test_notificacion_correo():
    destinatario = "test@example.com"
    asunto = "Prueba"
    mensaje = "Este es un mensaje de prueba"
    
    notificacion = NotificacionCorreo(destinatario, asunto, mensaje)
    
    assert notificacion.destinatario == destinatario
    assert notificacion.asunto == asunto
    assert notificacion.mensaje == mensaje
    
    # Simulamos el envío sin esperar que haga output real (pudiendo usar un mock en proyectos más avanzados)
    notificacion.enviar_notificacion()

# Test para NotificacionSMS
def test_notificacion_sms():
    numero = "555-1234"
    mensaje = "Este es un mensaje de prueba por SMS"
    
    notificacion = NotificacionSMS(numero, mensaje)
    
    assert notificacion.numero == numero
    assert notificacion.mensaje == mensaje
    
    # Simulamos el envío
    notificacion.enviar_notificacion()

# Test para NotificacionWhatsapp
def test_notificacion_whatsapp():
    numero = "555-5678"
    mensaje = "Este es un mensaje de prueba por WhatsApp"
    
    notificacion = NotificacionWhatsapp(numero, mensaje)
    
    assert notificacion.numero == numero
    assert notificacion.mensaje == mensaje
    
    # Simulamos el envío
    notificacion.enviar_notificacion()
