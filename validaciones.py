def validar_dni(numero):      
    if numero is None:
        return False
    if type(numero) != int:
        return False
    if numero  >= 27019996 and numero <= 47019996:
        return True
    return False

def validar_salario(numero):
    if numero is None:
        return False
    if type(numero) != int:
        return False
    if numero > 234315:
        return True
    return False
    

def validar_texto(caracteres):
    partes_palabra = caracteres.split()
    for parte in partes_palabra:
        if type(parte) != str:
            return False
    if len(caracteres) <= 20:
        return True
    return False


def validar_puesto(puesto):
    if puesto is None or not puesto.strip():
        return False
    puestos_validos = ["gerente", "supervisor", "analista", "encargado", "asistente"]
    puesto = puestos_validos
    if puesto in puestos_validos:
        return True
    return False

