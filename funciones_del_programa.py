from funciones import *
from validaciones import *
from datetime import datetime
from archivos import *



def crear_empleado(id: int, nombre: str, apellido: str, dni: str, puesto: str, salario: float) -> dict:
    
    """
    Crea un diccionario que representa a un empleado con los datos proporcionados.

    Args:
        id (int): El identificador único del empleado.
        nombre (str): El nombre del empleado.
        apellido (str): El apellido del empleado.
        dni (str): El número de DNI del empleado.
        puesto (str): El puesto de trabajo del empleado.
        salario (float): El salario del empleado.

    Returns:
        dict: Un diccionario que contiene la información del empleado.
    """

    diccionario_empleado = {
        "id": id,
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "puesto": puesto,
        "salario": salario
    }
    return diccionario_empleado

def ingresar_empleado(lista_empleados, contador_empleados_id):
    
    """
    Permite ingresar un nuevo empleado a una lista de empleados, con un límite de 20 empleados.

    Args:
        lista_empleados (list): La lista de empleados existente.
        contador_empleados_id (int): El contador de identificadores de empleados.

    Returns:
        tuple: Una tupla que contiene la lista actualizada de empleados y el contador de identificadores.
    """

    if len(lista_empleados) < 20:
        nombre = get_str("Nombre del empleado: ", validar_texto)
        apellido = get_str("Apellido del empleado: ", validar_texto)
        dni = get_int(validar_dni)
        puesto = get_puestos(validar_puesto)
        salario = get_int_dos()
        
        nuevo_empleado = crear_empleado(contador_empleados_id, nombre,apellido, dni,puesto,salario)
        lista_empleados.append(nuevo_empleado)
        contador_empleados_id += 1
        guardar_empleados_en_csv(lista_empleados)
        return lista_empleados, contador_empleados_id
    else:
        print("Límite de 20 empleados alcanzado, solo podrá ingresar más empleados si existe una vacante")
    return lista_empleados, contador_empleados_id

def mostrar_lista_empleados(lista_empleados):
    """
    Imprime una lista de empleados con su información.

    Args:
        lista_empleados (list): La lista de empleados a mostrar.
    """

    if lista_empleados:
        print(f'{"ID":<10} {"Nombre":<20} {"Apellido":<20} {"DNI":<10} {"Puesto":<20} {"Salario":<10}')
        for empleado in lista_empleados:
            print(f'{empleado["id"]:<10} {empleado["nombre"]:<20} {empleado["apellido"]:<20} {empleado["dni"]:<10} {empleado["puesto"]:<20} {empleado["salario"]:<10}')
    else:
        print("No hay empleados en la lista.")

def mostrar_un_empleado(un_empleado: dict):
    
    """
    Imprime la información de un solo empleado.

    Args:
        un_empleado (dict): Un diccionario que contiene la información de un empleado.
    """

    print(f'{"ID":<10} {"Nombre":<20} {"Apellido":<20} {"DNI":<10} {"Puesto":<20} {"Salario":<10}')
    print(f'{un_empleado["id"]:<10} {un_empleado["nombre"]:<20} {un_empleado["apellido"]:<20} {un_empleado["dni"]:<10} {un_empleado["puesto"]:<20} {un_empleado["salario"]:<10}')

def deshacer_ultimo_cambio(id, lista_empleados, historial):
   
    """
    Deshace el último cambio realizado a un empleado, utilizando un historial de cambios.

    Args:
        id (int): El identificador único del empleado.
        lista_empleados (list): La lista de empleados.
        historial (dict): Un diccionario que contiene el historial de cambios de los empleados.
    """

    if id in historial:
        ultimo_cambio = historial[id].pop()
        for empleado in lista_empleados:
            if empleado["id"] == id:
                empleado.update(ultimo_cambio)
        print("Último cambio deshecho exitosamente.")
    else:
        print("No hay cambios que deshacer.")

def modificar_empleado(id: int, lista_empleados, historial): 
    """
    Permite modificar la información de un empleado.

    Args:
        id (int): El identificador único del empleado.
        lista_empleados (list): La lista de empleados.
        historial (dict): Un diccionario que contiene el historial de cambios de los empleados.
    """

    empleado_encontrado = False
    for empleado in lista_empleados:
        if empleado["id"] == id:
            empleado_encontrado = True
            historial[id] = historial.get(id, [])  
            historial[id].append(empleado) 
            
            print("Empleado encontrado:")
            mostrar_un_empleado(empleado)
            print("¿Qué campo deseas modificar?")
            print("1. Salario")
            print("2. Nombre")
            print("3. Apellido")
            print("4. DNI")
            print("5. Puesto")
            opcion = input("Ingresa el número de la opción: ")

            opciones = {"1": "Salario", "2": "Nombre", "3": "Apellido", "4": "DNI", "5": "Puesto"}  

            if opcion == "1":
                nuevo_valor = get_int(validar_salario, "Ingrese el nuevo salario: ")
                empleado["salario"] = nuevo_valor
            elif opcion == "2":
                nuevo_valor = get_str("Nuevo nombre: ", validar_texto)
                empleado["nombre"] = nuevo_valor
            elif opcion == "3":
                nuevo_valor = get_str("Nuevo apellido: ", validar_texto)
                empleado["apellido"] = nuevo_valor
            elif opcion == "4":
                nuevo_valor = get_int(validar_dni, "Ingrese el nuevo DNI: ")
                empleado["dni"] = nuevo_valor
            elif opcion == "5":
                nuevo_valor = get_puestos(validar_puesto)
                empleado["puesto"] = nuevo_valor
            else:
                print("Opción no válida.")
                continue 
            print(f"El campo '{opciones[opcion]}' ha sido modificado exitosamente.")
            guardar_empleados_en_csv(lista_empleados)
            break 
    if  empleado_encontrado is False:  
        print("Empleado no encontrado.")
        return
        
    print("¿Desea deshacer el último cambio?")
    print("1. Si")
    print("2. No")
    opcion_deshacer = int(input("Ingresa el numero de la opcion: "))
    if opcion_deshacer == 1:
        deshacer_ultimo_cambio(id, lista_empleados)
    elif opcion_deshacer == 2:
        print("Continuar...")


def buscar_empleado_por_dni_apellido(lista_empleados):
    
    """
    Busca un empleado por su DNI, apellido o puesto y muestra su información.

    Args:
        lista_empleados (list): La lista de empleados en la que se realizará la búsqueda.
    """

    print("Seleccione una opcion de busqueda: ")
    print("1. Busqueda por DNI")
    print("2. Busqueda por Apellido")
    print("3. Busqueda por Puesto")

    opcion = int(input("Ingresa el número de la opción: "))

    if opcion == 1:
        dni = input("Ingrese el DNI del empleado: ")
        for empleado in lista_empleados:
            if empleado['dni'] == dni:
                mostrar_un_empleado(empleado)
                return
        print("Empleado no encontrado.")
    elif opcion == 2:
        apellido = input("Ingrese el apellido del empleado: ")
        for empleado in lista_empleados:
            if empleado["apellido"].lower() == apellido.lower():
                mostrar_un_empleado(empleado)
                return
        print("Empleado no encontrado")
    elif opcion == 3:
        puesto = input("Ingrese el puesto del empleado: ")
        for empleado in lista_empleados:
            if empleado["puesto"] == puesto:
                mostrar_un_empleado(empleado)
                return
        print("Empleado no encontrado")
    else:
        print("Opcion no valida. ")

#def eliminar_empleado(lista_empleados, lista_empleados_eliminados, id, empleados_no_eliminados):
    #for empleado in lista_empleados:
     #   if empleado["id"] == id:
      #      confirmacion = input(f"Estás a punto de eliminar al empleado con el ID {id}, ¿Estás seguro? s/n: ")
       #     if confirmacion.lower() == "s":
        #        empleado["eliminado"] = True
         #       print(f"Empleado con ID {id} marcado como eliminado.")
          #      lista_empleados_eliminados.append(empleado)
           # else:
            #    print("Eliminación cancelada.")
            #empleado_encontrado = True
        #else:
         #   empleados_no_eliminados.append(empleado)

    #if  empleado_encontrado is None :
     #   print("Empleado no encontrado.")
    #return None

def eliminar_empleado(lista_empleados, id, empleados_eliminados, empleados_no_eliminados): 
    """
    Marca a un empleado como eliminado y lo mueve a una lista de empleados eliminados.

    Args:
        lista_empleados (list): La lista de empleados.
        id (int): El identificador único del empleado a eliminar.
        empleados_eliminados (list): La lista de empleados marcados como eliminados.
        empleados_no_eliminados (list): La lista de empleados que no fueron eliminados.

    Returns:
        tuple: Una tupla que contiene las listas actualizadas de empleados eliminados y no eliminados.
    """
        
    empleado_encontrado = False
    for empleado in lista_empleados:
        if empleado["id"] == id:
            confirmacion = input(f"Estás a punto de eliminar al empleado con el ID {id}, ¿Estás seguro? s/n: ")
            if confirmacion.lower() == "s":
                empleado["eliminado"] = True
                print(f"Empleado con ID {id} marcado como eliminado.")
                empleados_eliminados.append(empleado)
            else:
                print("Eliminación cancelada.")
            empleado_encontrado = True
        else:
            empleados_no_eliminados.append(empleado)

    if  empleado_encontrado is False:
        print("Empleado no encontrado.") 
    return empleados_no_eliminados, empleados_eliminados


def calcular_salario_promedio(lista_empleados):
    """
    Calcula el salario promedio de los empleados en una lista.

    Args:
        lista_empleados (list): La lista de empleados.

    Returns:
        float: El salario promedio de los empleados.
    """

    if len(lista_empleados) == 0:
        return 0
    suma_salarios = sum(int(empleado["salario"]) for empleado in lista_empleados)
    promedio_salarios = suma_salarios / len(lista_empleados)
    return promedio_salarios

#def ordenar_y_mostrar_empleados(lista_empleados, ordenados):
    print("¿Cómo deseas ordenar la lista de empleados?")
    print("1. Por nombre")
    print("2. Por apellido")
    print("3. Por salario")
    opcion = input("Ingresa el número de la opción: ")

    if opcion == "1":
        criterio = "nombre"
    elif opcion == "2":
        criterio = "apellido"
    elif opcion == "3":
        criterio = "salario"
    else:
        print("Opción no válida.")
        return

    print("¿En qué dirección deseas ordenar la lista?")
    print("1. Ascendente")
    print("2. Descendente")
    direccion = input("Ingresa el número de la opción: ")

    if direccion == "1":
        reverse = False
    elif direccion == "2":
        reverse = True
    else:
        print("Dirección no válida.")
        return

    for empleado in lista_empleados:
        i = 0
        while i < len(ordenados):
            if empleado[criterio] > ordenados[i][criterio]:
                i += 1
            else:
                break
        ordenados.insert(i, empleado)
    mostrar_lista_empleados(ordenados)

def ordenar_por_criterio_burbujeo(lista_empleados, criterio, direccion, orden, orden_inverso):
    """
    Ordena la lista de empleados según un criterio mediante el algoritmo de burbujeo, ascendente o descendente.

    Args:
        lista_empleados (list): La lista de empleados a ordenar.
        criterio (str): El criterio por el cual ordenar la lista (por ejemplo, "nombre", "apellido", "salario").
        direccion (str): La dirección en la que ordenar la lista ("ascendente" o "descendente").
        orden (list): Una lista vacía que se utilizará para almacenar el resultado ordenado en orden ascendente.
        orden_inverso (list): Una lista vacía que se utilizará para almacenar el resultado ordenado en orden descendente.
    """
        
    empleado = len(lista_empleados)
    for i in range(empleado - 1):
        for j in range(0, empleado - i - 1):
            if lista_empleados[j][criterio] > lista_empleados[j + 1][criterio]:
                lista_empleados[j], lista_empleados[j + 1] = lista_empleados[j + 1], lista_empleados[j]
            elif lista_empleados[j][criterio] == lista_empleados[j + 1][criterio]:
                if lista_empleados[j]["id"] > lista_empleados[j + 1]["id"]:
                    lista_empleados[j], lista_empleados[j + 1] = lista_empleados[j + 1], lista_empleados[j]
        
        if direccion == "descendente":  
            for i in range(len(lista_empleados) - 1, -1, -1):
                orden_inverso.append(lista_empleados[i])
            mostrar_lista_empleados(orden_inverso)
        if direccion == "ascendente":
            
            for i in range(len(lista_empleados)):
                orden.append(lista_empleados[i])
            mostrar_lista_empleados(orden)

