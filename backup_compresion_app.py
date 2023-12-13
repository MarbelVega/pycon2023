import os
import subprocess
import datetime

def backup_django_project():
    # Asegúrate de estar en el directorio correcto
    os.chdir('/ruta/a/tu/proyecto')

    # Obtener la fecha y hora actual para el nombre del archivo de backup
    now = datetime.datetime.now()
    backup_name = f"backup_{now.strftime('%Y%m%d_%H%M%S')}"

    # Crear un archivo tar.gz con el contenido del proyecto
    subprocess.run(["tar", "-czf", f"{backup_name}.tar.gz", "."])

# Llamar a la función
backup_django_project()