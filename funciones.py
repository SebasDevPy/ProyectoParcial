import validaciones

def get_int(validacion):
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
    while True:
        try:
            puesto = input("Ingrese el puesto: Gerente, Supervisor, Analista, Encargado o Asistente: ")
            if validacion(puesto):
                return puesto.capitalize()
            else:
                print("Error, el puesto debe ser uno de los siguientes: Gerente, Supervisor, Analista, Encargado o Asistente")
        except ValueError:
            print("Error, el puesto debe ser uno de los siguientes: Gerente, Supervisor, Analista, Encargado o Asistente")




