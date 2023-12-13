import os
import subprocess
import shutil

# Crear un nuevo entorno virtual
subprocess.run(["python3", "-m", "venv", "nuevo_entorno"])

# Activar el entorno virtual
activate_this_file = os.path.join(os.getcwd(), "nuevo_entorno/bin/activate_this.py")
exec(open(activate_this_file).read(), {'__file__': activate_this_file})

# Migrar la carpeta con el código al nuevo proyecto
shutil.copytree('antiguo_proyecto', 'nuevo_entorno', dirs_exist_ok=True)

# Instalar la nueva versión de Django
subprocess.run(["pip", "install", "--upgrade", "Django==nueva_version"])