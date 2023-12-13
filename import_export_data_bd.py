import sqlite3
import csv

# Conectar a la base de datos
conn = sqlite3.connect('mi_base_de_datos.db')
c = conn.cursor()

# Exportar datos a un archivo CSV
with open('export.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for row in c.execute('SELECT * FROM mi_tabla'):
        writer.writerow(row)

# Importar datos desde un archivo CSV
with open('import.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        c.execute("INSERT INTO mi_tabla VALUES (?, ?, ?)", row)

# Guardar (commit) los cambios
conn.commit()

# Cerrar la conexión con la base de datos
conn.close()