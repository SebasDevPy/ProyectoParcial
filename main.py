from funciones_del_programa import *


def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Ingresar empleado")
    print("2. Modificar empleado")
    print("3. Eliminar empleado")
    print("4. Mostrar lista de empleados")
    print("5. Calcular salario promedio")
    print("6. Buscar empleado")
    print("7. Ordenar y mostrar empleados")
    print("8. Generar reporte de empleados por sueldo")
    print("9. Generar reporte de empleado por apellido")
    print("10. Salario promedio de los empleados.")
    print("10. Salir")

def main():
    lista_empleados, contador_empleados_id = leer_empleados_desde_csv([], 0)
    lista_empleados_eliminados = cargar_empleados_eliminados_desde_json([])
    reporte_contador_sueldo = 0
    reporte_contador_apellido = 0
    historial = {}
    empleado_encontrado = None    
    empleados_no_eliminados = []
    orden_inverso = []
    orden = []
    # lista filtrada/copia de la lista original:  lista_empleados[:] = empleados_no_eliminados 
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            lista_empleados, contador_empleados_id = ingresar_empleado(lista_empleados, contador_empleados_id)
        elif opcion == "2":
            id_modificar = int(input("Ingrese el ID del empleado a modificar: "))
            modificar_empleado(id_modificar, lista_empleados, historial)  
        elif opcion == "3":
            #id_eliminar = int(input("Ingrese el ID del empleado a eliminar: "))
            #eliminar_empleado(lista_empleados, lista_empleados_eliminados, id_eliminar, empleados_no_eliminados)
            #lista_empleados[:] = empleados_no_eliminados
            #empleados_no_eliminados.clear()
            id_eliminar = int(input("Ingrese el ID del empleado a eliminar: "))
            lista_empleados, empleados_eliminados = eliminar_empleado(lista_empleados, id_eliminar, empleados_eliminados, empleados_no_eliminados)
        elif opcion == "4":
            mostrar_lista_empleados(lista_empleados)
        elif opcion == "5":
            promedio_salarios = calcular_salario_promedio(lista_empleados)
            print(f"El salario promedio de los empleados es: {promedio_salarios}")
        elif opcion == "6":
            buscar_empleado_por_dni_apellido(lista_empleados)
        elif opcion == "7":
            #ordenar_y_mostrar_empleados(lista_empleados, ordenados)
            criterio = input("Ingrese el criterio de ordenacion: nombre, apellido o salario: ")
            direccion = input("Ingrese si quiere el orden de forma ascendente o descendente: ")
            ordenar_por_criterio_burbujeo(lista_empleados, criterio, direccion, orden, orden_inverso)
        elif opcion == "8":
            sueldo = float(input("Ingrese el sueldo para generar el reporte: "))
            generar_reporte_empleados_sueldo(lista_empleados, sueldo, reporte_contador_sueldo)
            reporte_contador_sueldo += 1
        elif opcion == "9":
            apellido = input("Ingrese el apellido del empleado: ") 
            generar_reporte_por_apellido(lista_empleados, apellido, reporte_contador_apellido)
            reporte_contador_apellido += 1
        elif opcion == "10":
            print("Saliendo del programa...")
            guardar_empleados_en_csv(lista_empleados)
            guardar_empleados_eliminados_en_json(lista_empleados_eliminados)
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción del menú.")

if __name__ == "__main__":
    main()