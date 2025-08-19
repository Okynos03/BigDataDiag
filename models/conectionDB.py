import mysql.connector

# Crear la conexión a MySQL
conexion = mysql.connector.connect(
    host="localhost",        # Dirección del servidor MySQL
    user="adminDB",             # Usuario de MySQL
    password="5860",# Contraseña del usuario
    database="employeesdb"       # Nombre de la base de datos
)
# Crear cursor
cursor = conexion.cursor()

# Consultar datos
cursor.execute("SELECT emp_no, first_name, last_name, gender, hire_date FROM employees limit 10")
for fila in cursor.fetchall():
    print(fila)

# Cerrar cursor y conexión
cursor.close()
conexion.close()
