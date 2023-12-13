import shutil

# Copiar archivo de src a dst. (cp src dst)
shutil.copy('ruta/al/archivo/fuente', 'ruta/al/archivo/destino')

# Copiar archivo de src a dst, pero preservar metadatos. (cp -p src dst)
shutil.copy2('ruta/al/archivo/fuente', 'ruta/al/archivo/destino')

# Mover archivo de src a dst. (mv src dst)
shutil.move('ruta/al/archivo/fuente', 'ruta/al/archivo/destino')