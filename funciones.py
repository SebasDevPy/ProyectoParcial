import validaciones

def get_int(validacion):
    while True:
        numero = int(input("Ingrese su DNI sin puntos: "))
        if validacion(numero):
            return str(numero)
        else:
            print("Ingrese correctamente su DNI")

def get_int_dos():
    while True:
        numero = int(input("Ingrese el salario: "))
        if validaciones.validar_salario(numero):
            return str(numero)
        else:
            print("El salario debe de ser igual o mayor a $234315.")

def get_str(prompt, validacion):
    while True:
        s = input(prompt)
        if validacion(s):
            return s
        else:
            print("Entrada no válida, no puede contener más de 20 caracteres, números ni caracteres especiales")

def get_puestos(validacion):
    while True:
        puesto = input("Ingrese el puesto: Gerente, Supervisor, Analista, Encargado o Asistente: ")
        if validacion(puesto):
            return puesto.capitalize()
        else:
            print("Error, el puesto debe ser uno de los siguientes: Gerente, Supervisor, Analista, Encargado o Asistente")




