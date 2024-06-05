from validaciones import *

def get_int(validacion):
    """
    Solicita al usuario ingresar un número entero y valida la entrada utilizando una función de validación.

    Args:
        validacion (function): Una función que toma un entero como argumento y devuelve True si la entrada es válida, de lo contrario False.

    Returns:
        str: El número entero ingresado como una cadena si pasa la validación.
    """
        
    while True:
        try:
            numero = int(input("Ingrese su DNI sin puntos: "))
            if validacion(numero):
                return str(numero)
            else:
                print("Ingrese correctamente su DNI")
        except ValueError:
            print("Ingrese un numero valido")


def get_int_dos(validacion):
    """
    Solicita al usuario ingresar un número entero y valida la entrada utilizando una función de validación.

    Args:
        validacion (function): Una función que toma un entero como argumento y devuelve True si la entrada es válida, de lo contrario False.

    Returns:
        str: El número entero ingresado como una cadena si pasa la validación.
    """

    while True:
        try:
            numero = int(input("Ingrese el salario: "))
            if validacion(numero):
                return str(numero)
            else:
                print("El salario debe de ser igual o mayor a $234315.")
        except ValueError:
            print("Ingrese un monto superior a: $234315")

def get_str(prompt, validacion):
    """
    Solicita al usuario ingresar una cadena de texto y valida la entrada utilizando una función de validación.

    Args:
        prompt (str): El mensaje que se muestra al usuario para solicitar la entrada.
        validacion (function): Una función que toma una cadena de texto como argumento y devuelve True si la entrada es válida, de lo contrario False.

    Returns:
        str: La cadena de texto ingresada por el usuario si pasa la validación.
    """
        
    while True:
        try:
            mensaje = input(prompt)
            if validacion(mensaje):
                return mensaje
            else:
                print("Entrada no válida, no puede contener más de 20 caracteres, números ni caracteres especiales")
        except ValueError:
            print("Entrada no válida, no puede contener más de 20 caracteres, números ni caracteres especiales")

def get_puestos(validacion):
    """
    Solicita al usuario ingresar un puesto y valida la entrada utilizando una función de validación.

    Args:
        validacion (function): Una función que toma una cadena de texto como argumento y devuelve True si la entrada es válida, de lo contrario False.

    Returns:
        str: El puesto ingresado por el usuario si pasa la validación.
    """
        
    while True:
        try:
            puesto = input("Ingrese el puesto: Gerente, Supervisor, Analista, Encargado o Asistente: ")
            if validacion(puesto):
                return puesto.capitalize()
            else:
                print("Error, el puesto debe ser uno de los siguientes: Gerente, Supervisor, Analista, Encargado o Asistente")
        except ValueError:
            print("Error, el puesto debe ser uno de los siguientes: Gerente, Supervisor, Analista, Encargado o Asistente")




