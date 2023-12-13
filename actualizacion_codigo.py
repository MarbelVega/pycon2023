import os
import subprocess

def git_commit_push():
    # Asegúrate de estar en el directorio correcto
    os.chdir('/ruta/a/tu/proyecto')

    # Agregar todos los archivos modificados al staging area
    subprocess.run(["git", "add", "."])

    # Hacer commit de los cambios
    commit_message = "Actualización automática del proyecto Django"
    subprocess.run(["git", "commit", "-m", commit_message])

    # Hacer push de los cambios al repositorio remoto
    subprocess.run(["git", "push"])

# Llamar a la función
git_commit_push()