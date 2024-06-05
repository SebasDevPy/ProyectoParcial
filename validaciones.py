def validar_dni(numero):      
    """
    Valida si un número de DNI es válido.

    Args:
        numero (int): El número de DNI a validar.

    Returns:
        bool: True si el DNI es válido, False en caso contrario.
    """
        
    if numero is None:
        return False
    if type(numero) != int:
        return False
    if numero  >= 27019996 and numero <= 47019996:
        return True
    return False

def validar_salario(numero):
    """
    Valida si un monto de salario es válido.

    Args:
        numero (int): El monto de salario a validar.

    Returns:
        bool: True si el salario es válido, False en caso contrario.
    """
        
    if numero is None:
        return False
    if type(numero) != int:
        return False
    if numero > 234315:
        return True
    return False
    

def validar_texto(caracteres):
    """
    Valida si una cadena de texto cumple con ciertas condiciones.

    Args:
        caracteres (str): La cadena de texto a validar.

    Returns:
        bool: True si la cadena de texto es válida, False en caso contrario.
    """
        
    partes_palabra = caracteres.split()
    for parte in partes_palabra:
        if type(parte) != str:
            return False
    if len(caracteres) <= 20:
        return True
    return False


def validar_puesto(puesto):
    """
    Valida si un puesto laboral es válido.

    Args:
        puesto (str): El puesto laboral a validar.

    Returns:
        bool: True si el puesto es válido, False en caso contrario.
    """
        
    if puesto is None or not puesto.strip():
        return False
    puestos_validos = ["gerente", "supervisor", "analista", "encargado", "asistente"]
    puesto = puestos_validos
    if puesto.lower() in puestos_validos:
        return True
    return False

