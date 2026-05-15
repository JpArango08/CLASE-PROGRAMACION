"""
Ejemplo basico de conexion a PostgreSQL desde Python

"""
import psycopg2

# Reemplace los datos de conexion con los datos tomados de su servidor
connection = psycopg2.connect(database="credit_card_0k3w", user="credit_card_0k3w_user", password="7KFpyf5Vccck3RUMMtwetwEkD55i4IOq", host="dpg-d7ln3i9o3t8c73f8g6j0-a.oregon-postgres.render.com", port=5432)
nombre_municipio= str(input("Ingrese un municipio a buscar: "))
# Todas las instrucciones se ejecutan a tavés de un cursor
cursor = connection.cursor()
sql= f"SELECT codigo_departamento from municipios where nombre_municipio like '{nombre_municipio}%';"
cursor.execute(sql)

# Si la instruccion retorna resultados, se accede a ellos con fetchone() o fetchall()  segun la necesidad
record = cursor.fetchall()

print("Resultados : ")

# El resultado de fetchall() es una lista de tuplas
print(record)