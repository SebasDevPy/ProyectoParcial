from funciones import *
from validaciones import *
from datetime import datetime
from archivos import *



def crear_empleado(id: int, nombre: str, apellido: str, dni: str, puesto: str, salario: float) -> dict:
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
    if lista_empleados:
        print(f'{"ID":<10} {"Nombre":<20} {"Apellido":<20} {"DNI":<10} {"Puesto":<20} {"Salario":<10}')
        for empleado in lista_empleados:
            print(f'{empleado["id"]:<10} {empleado["nombre"]:<20} {empleado["apellido"]:<20} {empleado["dni"]:<10} {empleado["puesto"]:<20} {empleado["salario"]:<10}')
    else:
        print("No hay empleados en la lista.")

def mostrar_un_empleado(un_empleado: dict):
    print(f'{"ID":<10} {"Nombre":<20} {"Apellido":<20} {"DNI":<10} {"Puesto":<20} {"Salario":<10}')
    print(f'{un_empleado["id"]:<10} {un_empleado["nombre"]:<20} {un_empleado["apellido"]:<20} {un_empleado["dni"]:<10} {un_empleado["puesto"]:<20} {un_empleado["salario"]:<10}')

def deshacer_ultimo_cambio(id, lista_empleados, historial):
    if id in historial:
        ultimo_cambio = historial[id].pop()
        for empleado in lista_empleados:
            if empleado["id"] == id:
                empleado.update(ultimo_cambio)
        print("Último cambio deshecho exitosamente.")
    else:
        print("No hay cambios que deshacer.")

def modificar_empleado(id: int, lista_empleados, historial, empleado_encontrado): 
    try:
        for empleado in lista_empleados:
            if empleado["id"] == id:
                empleado_encontrado = empleado
                if id in historial:
                    historial[id].append(empleado.copy())
                else:
                    historial[id] = [empleado.copy()]
                
                def confirmar_cambio(campo, nuevo_valor):
                    confirmacion = input(f"Estás a punto de cambiar el {campo} a {nuevo_valor}. ¿Estás seguro? (s/n): ")
                    if confirmacion.lower() == 's':
                        empleado[campo] = nuevo_valor
                        print(f"El {campo} ha sido modificado exitosamente.")
                        guardar_empleados_en_csv(lista_empleados)
                    else:
                        print(f"La modificación del {campo} ha sido cancelada.")
                
                print("Empleado encontrado")
                print("¿Qué elemento deseas modificar?")
                print("1. Salario")
                print("2. Nombre")
                print("3. Apellido")
                print("4. DNI")
                print("5. Puesto")
                opcion = int(input("Ingresa el número de la opción: "))

                if opcion == 1:
                    nuevo_valor = get_int(validar_salario, "Ingrese el nuevo salario: ")
                    confirmar_cambio("salario", nuevo_valor)
                elif opcion == 2:
                    nuevo_valor = get_str("Nuevo nombre: ", validar_texto)
                    confirmar_cambio("nombre", nuevo_valor)
                elif opcion == 3:
                    nuevo_valor = get_str("Nuevo apellido: ", validar_texto)
                    confirmar_cambio("apellido", nuevo_valor)
                elif opcion == 4:
                    nuevo_valor = get_int(validar_dni, "Ingrese el nuevo DNI: ")
                    confirmar_cambio("dni", nuevo_valor)
                elif opcion == 5:
                    nuevo_valor = get_puestos(validar_puesto)
                    confirmar_cambio("puesto", nuevo_valor)
                else:
                    print("Opción no válida.")
                break
        if empleado_encontrado is None:
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
    except ValueError as e:
        print("Error:", e)

def buscar_empleado_por_dni_apellido(lista_empleados):
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

def eliminar_empleado(lista_empleados, lista_empleados_eliminados, id, empleados_no_eliminados):
    for empleado in lista_empleados:
        if empleado["id"] == id:
            confirmacion = input(f"Estás a punto de eliminar al empleado con el ID {id}, ¿Estás seguro? s/n: ")
            if confirmacion.lower() == "s":
                empleado["eliminado"] = True
                print(f"Empleado con ID {id} marcado como eliminado.")
                lista_empleados_eliminados.append(empleado)
            else:
                print("Eliminación cancelada.")
            empleado_encontrado = True
        else:
            empleados_no_eliminados.append(empleado)

    if  empleado_encontrado is None :
        print("Empleado no encontrado.")
    return None

#  def eliminar_empleado(lista_empleados, id, empleados_eliminados, empleados_no_eliminados)  
# empleado_encontrado = False
    #for empleado in lista_empleados:
     #   if empleado["id"] == id:
      #      confirmacion = input(f"Estás a punto de eliminar al empleado con el ID {id}, ¿Estás seguro? s/n: ")
       #     if confirmacion.lower() == "s":
        #        empleado["eliminado"] = True
         #       print(f"Empleado con ID {id} marcado como eliminado.")
          #      empleados_eliminados.append(empleado)
           # else:
            #    print("Eliminación cancelada.")
            #empleado_encontrado = True
        #else:
         #   empleados_no_eliminados.append(empleado)

    #if  empleado_encontrado is None:
     #   print("Empleado no encontrado.")
    
    #return empleados_no_eliminados, empleados_eliminados


def calcular_salario_promedio(lista_empleados):
    if len(lista_empleados) == 0:
        return 0
    suma_salarios = sum(int(empleado["salario"]) for empleado in lista_empleados)
    promedio_salarios = suma_salarios / len(lista_empleados)
    return promedio_salarios

def ordenar_y_mostrar_empleados(lista_empleados):
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

    lista_empleados.sort(key=lambda empleado: empleado[criterio], reverse=reverse)
    mostrar_lista_empleados(lista_empleados)


        

