class empleado:
    def __init__(self,codigo,nombre,departamento,tiempo):
        self.codigo = codigo
        self.nombre = nombre
        self.departamento = departamento
        self.tiempo = tiempo


class evaluacion:
    def __init__(self,codigo,nombre,puntualidad,equipo,productividad):
        self.codigo = codigo
        self.nombre = nombre
        self.puntualidad = puntualidad
        self.equipo = equipo
        self.productividad = productividad

class contacto:
    def __init__(self,codigo,nombre,email,telefono):
        self.codigo = codigo
        self.nombre = nombre
        self.email = email
        self.telefono = telefono


empleados = {}
opcion = 0
while opcion !=5:
    print("=== REGISTRO EMPLEADO ===")
    print("1. Registro Empleado")
    print("2. Mostrar datos")
    print("3. Promedio empleado")
    print("4. Desempeño empleado")
    print("5. Salir")
    opcion = int(input("Seleccione una opcion: "))
