import os
import subprocess

def iniciar_servicio():
    os.chdir('/ruta/a/tu/proyecto/django')  # Cambia al directorio del proyecto Django
    subprocess.Popen(['python', 'manage.py', 'runserver'])  # Inicia el servidor Django

def detener_servicio():
    subprocess.run(['pkill', '-f', 'runserver'])  # Detiene el servidor Django

def reiniciar_servicio():
    detener_servicio()
    iniciar_servicio()

# Ejemplo de uso:
iniciar_servicio()
# detener_servicio()
# reiniciar_servicio()