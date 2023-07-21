import pymysql

# Reemplaza 'tu_host_aquí', 'tu_usuario_aquí', 'tu_contraseña_aquí' y 'tu_base_de_datos_aquí' con los valores apropiados.
config = {
    'host': 'localhost',
    'user': 'root',
    'password': '8888',
    'database': 'mysql',
}

try:
    # Utilizamos pymysql.connect en lugar de mysql.connector.connect
    Database = pymysql.connect(**config)
    print("Conexión exitosa a la base de datos MySQL.")
    # Aquí va el resto de tu código relacionado con la base de datos

except pymysql.Error as err:
    print(f"Error: {err}")

