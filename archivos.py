import csv
import json
from datetime import datetime

def leer_empleados_desde_csv(lista_empleados, contador_empleados_id):
    """
    Lee los datos de los empleados desde un archivo CSV y los agrega a una lista.

    Args:
        lista_empleados (list): Lista que almacenará los empleados leídos.
        contador_empleados_id (int): Contador para el ID de los empleados.

    Returns:
        tuple: Una tupla con la lista actualizada de empleados y el nuevo contador de ID.
    """

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
    """
    Guarda la lista de empleados en un archivo CSV.

    Args:
        lista_empleados (list): Lista de empleados a guardar.
    """

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
    """
    Guarda la lista de empleados eliminados en un archivo JSON.

    Args:
        lista_empleados_eliminados (list): Lista de empleados eliminados a guardar.
    """
        
    try:
        with open('Bajas.json', mode='w') as file:
            json.dump(lista_empleados_eliminados, file, indent=4)
        print("Datos guardados correctamente en Bajas.json")
    except Exception as e:
        print(f"Error al guardar en el archivo Bajas.json: {e}")

def cargar_empleados_eliminados_desde_json(lista_empleados_eliminados):
    """
    Carga los datos de los empleados eliminados desde un archivo JSON.

    Args:
        lista_empleados_eliminados (list): Lista que almacenará los empleados eliminados leídos.

    Returns:
        list: Lista actualizada de empleados eliminados.
    """

    try:
        with open('Bajas.json', mode='r') as file:
            lista_empleados_eliminados = json.load(file)
        print("Datos cargados correctamente desde Bajas.json")
    except FileNotFoundError:
        print("Archivo Bajas.json no encontrado. Se iniciará con una lista vacía.")
    except Exception as e:
        print(f"Error al cargar los empleados eliminados desde el archivo JSON: {e}")
    return lista_empleados_eliminados


def generar_reporte_empleados_sueldo(lista_empleados, sueldo, reporte_contador_sueldo):
    """
    Genera un reporte de empleados con un salario mayor a un monto especificado.

    Args:
        lista_empleados (list): Lista de empleados.
        sueldo (float): Monto de salario para filtrar empleados.
        reporte_contador_sueldo (int): Contador de reportes generados.

    Returns:
        tuple: Una tupla con el contador actualizado de reportes y un booleano indicando éxito o fallo.
    """
        
    try:
        sueldo = float(sueldo)  
        empleados_filtrados = [empleado for empleado in lista_empleados if float(empleado["salario"]) > sueldo]
        fecha_actual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  
        nombre_reporte = f"Reporte_{reporte_contador_sueldo}_{fecha_actual}.txt"
        
        with open(nombre_reporte, 'w', encoding="utf-8") as file:
            file.write(f"Reporte de empleados con salario mayor a {sueldo}:\n\n")
            file.write(f"Reporte número: {reporte_contador_sueldo}\n")
            file.write(f"Fecha de solicitud: {fecha_actual}\n")
            file.write(f"Cantidad de empleados que superan el sueldo de {sueldo}: {len(empleados_filtrados)}\n\n")
            file.write(f'{"ID":<10} {"Nombre":<20} {"Apellido":<20} {"DNI":<10} {"Puesto":<20} {"Salario":<10}\n')
            for empleado in empleados_filtrados:
                file.write(f'{empleado["id"]:<10} {empleado["nombre"]:<20} {empleado["apellido"]:<20} {empleado["dni"]:<10} {empleado["puesto"]:<20} {empleado["salario"]:<10}\n')

        print(f"Reporte generado: {nombre_reporte}")
        return reporte_contador_sueldo + 1, True
    except ValueError:
        print("Error: El valor de sueldo no es válido. Por favor, ingrese un número válido.")
        return reporte_contador_sueldo, False
    
def generar_reporte_por_apellido(lista_empleados, apellido, reporte_contador_apellido):
    """
    Genera un reporte de empleados con un apellido específico.

    Args:
        lista_empleados (list): Lista de empleados.
        apellido (str): Apellido para filtrar empleados.
        reporte_contador_apellido (int): Contador de reportes generados.

    Returns:
        tuple: Una tupla con el contador actualizado de reportes y un booleano indicando éxito o fallo.
    """
        
    try:
        empleados_filtrados = [empleado for empleado in lista_empleados if empleado["apellido"].lower() == apellido.lower()]
        if len(empleados_filtrados) == 0:
            print(f"No se encontraron empleados con el apellido '{apellido}'.")
            return reporte_contador_apellido, False  
        
        reporte_contador_apellido += 1
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H-%M-%S")  
        nombre_reporte = f"Reporte_{reporte_contador_apellido}_{fecha_actual}.txt"
        
        with open(nombre_reporte, 'w', encoding="utf-8") as file:
            file.write(f"Reporte número: {reporte_contador_apellido}\n")
            file.write(f"Fecha de solicitud: {fecha_actual}\n")
            file.write(f"Cantidad de empleados con el apellido '{apellido}': {len(empleados_filtrados)}\n\n")
            file.write(f'{"ID":<10} {"Nombre":<20} {"Apellido":<20} {"DNI":<10} {"Puesto":<20} {"Salario":<10}\n')
            for empleado in empleados_filtrados:
                file.write(f'{empleado["id"]:<10} {empleado["nombre"]:<20} {empleado["apellido"]:<20} {empleado["dni"]:<10} {empleado["puesto"]:<20} {empleado["salario"]:<10}\n')

        print(f"Reporte generado: {nombre_reporte}")
        return reporte_contador_apellido, True 
    except ValueError:
        print("Error: El valor de sueldo no es válido. Por favor, ingrese un número válido.")
        return reporte_contador_apellido, False 