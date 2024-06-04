def validar_dni(numero):
    return 5000000 <= numero <= 99999999

def validar_salario(numero):
    return numero >= 234315

def validar_texto(caracteres):
    return all(parte.isalpha() for parte in caracteres.split()) and len(caracteres) <= 20

def validar_puesto(puesto):
    puestos_validos = ["gerente", "supervisor", "analista", "encargado", "asistente"]
    return puesto.lower() in puestos_validos

