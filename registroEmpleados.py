class empleado:
    def __init__(self,codigo,nombre,departamento,antiguedad):
        self.codigo = codigo
        self.nombre = nombre
        self.departamento = departamento
        self.antiguedad = antiguedad

    def mostrar_info(self):
        print(f"nombre: {self.nombre}, departamento: {self.departamento}, antiguedad: {self.antiguedad}")


class evaluacion:
    def __init__(self,puntualidad,equipo,productividad,observacion):
        self.puntualidad = puntualidad
        self.equipo = equipo
        self.productividad = productividad
        self.observacion = observacion

    def calcular_promedio(self):
        return (self.puntualidad + self.equipo + self.productividad) / 3

    def mostrar_info(self):
        print(f"Puntualidad: {self.puntualidad}, Equipo: {self.equipo}, Productividad: {self.productividad}")
        print(f"Observación: {self.observacion}")
        print(f"Promedio: {self.calcular_promedio():.2f}")

class contacto:
    def __init__(self,email,telefono):
        self.email = email
        self.telefono = telefono

        def mostrar_info(self):
            print(f"Email: {self.email}, Teléfono: {self.telefono}")


empleados = {}
opcion = 0
while opcion !=5:
    print("=== REGISTRO EMPLEADO ===")
    print("1. Registro Empleado")
    print("2. Mostrar datos")
    print("3. Promedio empleado")
    print("4. Desempeño empleado")
    print("5. Salir")
    try:
        opcion = int(input("Seleccione una opcion: "))
    except ValueError:
        print("Opcion no valida")
        continue

    if opcion == 1:
        print("Registro Empleado")
        cantidad = int(input("Cuantos empleados desea registrar?: "))
        for c in range(cantidad):
            codigo = input("Codigo: ")
            nombre = input("Nombre: ")
            departamento = input("Departamento: ")
            antiguedad = input("Tiempo en la empresa: ")
            print("Calificacion por desempeño del empleado")
            puntualidad = int(input("Puntuacion en puntualidad: "))
            productividad = int(input("Puntuacion en Productividad: "))
            equipo = int(input("Puntuacion en Equipo: "))
            observacion = input("Observacion: ")
            telefono = input("Telefono: ")
            correo = input("Correo: ")

            empleado1 = empleado(codigo, nombre, departamento, antiguedad)
            evavaluacion1 = evaluacion(puntualidad, equipo, productividad, observacion)
            contacto1 = contacto(correo, telefono)

            empleados[codigo] = {
                "empleado": empleado1,
                "evaluacion": evavaluacion1,
                "contacto": contacto1
            }

    elif opcion == 2:
        print("Informacion Empleados")
        if not empleados:
            print("No hay empleados registrados.")
        for emp in empleados.values():
            emp["empleado"].mostrar_info()
            emp["evaluacion"].mostrar_info()
            emp["contacto"].mostrar_info()
