import sqlite3

# Crear una base de datos
conn = sqlite3.connect('mi_base_de_datos.db')

# Crear una tabla
c = conn.cursor()
c.execute('''CREATE TABLE mi_tabla
             (id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER)''')

# Insertar datos en la tabla
c.execute("INSERT INTO mi_tabla VALUES (1, 'Christian', 25)")

# Modificar datos en la tabla
c.execute("UPDATE mi_tabla SET edad = 26 WHERE nombre = 'Christian'")

# Eliminar datos de la tabla
c.execute("DELETE FROM mi_tabla WHERE nombre = 'Christian'")

# Guardar (commit) los cambios
conn.commit()

# Cerrar la conexión con la base de datos
conn.close()