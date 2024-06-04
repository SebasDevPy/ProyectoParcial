import csv
import json

def leer_empleados_desde_csv(lista_empleados, contador_empleados_id):

    try:
        with open('Empleados.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                empleado_id = int(row["id"])
                if empleado_id > contador_empleados_id:
                    contador_empleados_id = empleado_id
                empleado = {
                    "id": empleado_id,
                    "nombre": row["nombre"],
                    "apellido": row["apellido"],
                    "dni": row["dni"],
                    "puesto": row["puesto"],
                    "salario": float(row["salario"])
                }
                lista_empleados.append(empleado)
            contador_empleados_id += 1 
    except FileNotFoundError:
        print("Archivo Empleados.csv no encontrado. Se iniciará con una lista vacía.")
    except Exception as e:
        print(f"Error al leer el archivo Empleados.csv: {e}")
    return lista_empleados, contador_empleados_id

def guardar_empleados_en_csv(lista_empleados):
    try:
        with open('Empleados.csv', mode='w', newline='') as file:
            fieldnames = ["id", "nombre", "apellido", "dni", "puesto", "salario"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for empleado in lista_empleados:
                writer.writerow(empleado)
        print("Datos guardados correctamente en Empleados.csv")
    except Exception as e:
        print(f"Error al guardar en el archivo Empleados.csv: {e}")

def guardar_empleados_eliminados_en_json(lista_empleados_eliminados):
    try:
        with open('Bajas.json', mode='w') as file:
            json.dump(lista_empleados_eliminados, file, indent=4)
        print("Datos guardados correctamente en Bajas.json")
    except Exception as e:
        print(f"Error al guardar en el archivo Bajas.json: {e}")

def cargar_empleados_eliminados_desde_json(lista_empleados_eliminados):
    
    try:
        with open('Bajas.json', mode='r') as file:
            lista_empleados_eliminados = json.load(file)
        print("Datos cargados correctamente desde Bajas.json")
    except FileNotFoundError:
        print("Archivo Bajas.json no encontrado. Se iniciará con una lista vacía.")
    except Exception as e:
        print(f"Error al cargar los empleados eliminados desde el archivo JSON: {e}")
    return lista_empleados_eliminados