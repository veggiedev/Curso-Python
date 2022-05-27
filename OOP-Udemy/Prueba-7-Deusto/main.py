import sqlite3

conn = sqlite3.connect('grupos.db')

print('Conexion establecida correctamente')

cursor = conn.cursor()

# cursor.execute('CREATE TABLE rock (nombre text, miembros int)')

cursor.execute("INSERT INTO rock VALUES ('Kiss', 4)")

valores = [('Bon Jovi', 5), ('ACDC', 4), ('Muse', 3), ('The Cult', 4)]

cursor.executemany('INSERT INTO rock values(?, ?)', valores)

conn.commit()

conn.close()