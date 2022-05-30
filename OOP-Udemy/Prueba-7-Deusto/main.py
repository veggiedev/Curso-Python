import sqlite3

conn = sqlite3.connect('grupos.db')

print('Conexion establecida correctamente')

cursor = conn.cursor()


print('Ordenados por nombre de forma descendente:')
cursor.execute('SELECT * FROM rock ORDER BY miembros DESC')
lineas = cursor.fetchall()

for registro in lineas:
    print(registro)

# cursor.execute('CREATE TABLE rock (nombre text, miembros int)')

# cursor.execute("INSERT INTO rock VALUES ('Kiss', 4)")

# valores = [('Bon Jovi', 5), ('ACDC', 4), ('Muse', 3), ('The Cult', 4)]

# cursor.executemany('INSERT INTO rock values(?, ?)', valores)

# cursor.execute('SELECT * FROM rock WHERE miembros=3')
# lineas = cursor.fetchall()


# for registro in lineas:
#     print(registro[0])



conn.commit()

conn.close()