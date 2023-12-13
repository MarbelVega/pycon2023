#pip install virtualenv.
import os
import subprocess
import venv

def crear_entorno_virtual(ruta):
    venv.create(ruta, with_pip=True)

def instalar_django(ruta):
    subprocess.run([os.path.join(ruta, 'bin', 'pip'), 'install', 'django'])

def crear_proyecto_django(ruta, nombre_proyecto):
    subprocess.run([os.path.join(ruta, 'bin', 'django-admin'), 'startproject', nombre_proyecto])

def main():
    ruta_entorno_virtual = '/ruta/a/tu/entorno/virtual'
    nombre_proyecto = 'nombre_de_tu_proyecto'

    crear_entorno_virtual(ruta_entorno_virtual)
    instalar_django(ruta_entorno_virtual)
    crear_proyecto_django(ruta_entorno_virtual, nombre_proyecto)

if __name__ == '__main__':
    main()