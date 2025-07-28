class empleado:
    def __init__(self,codigo,nombre,departamento,antiguedad):
        self.codigo = codigo
        self.nombre = nombre
        self.departamento = departamento
        self.antiguedad = antiguedad

    def mostrar_info(self):
        print(f"nombre: {self.nombre}, departamento: {self.departamento}, antiguedad: {self.antiguedad}")


class evaluacion:
    def __init__(self,codigo,nombre,puntualidad,equipo,productividad,observacion,promedio):
        self.codigo = codigo
        self.nombre = nombre
        self.puntualidad = puntualidad
        self.equipo = equipo
        self.productividad = productividad
        self.observacion = observacion
        self.promedio = promedio

    def mostrar_info(self):
        print(f"puntualidad: {self.puntualidad}, equipo: {self.equipo}, productividad: {self.productividad}, "
              f"observacion: {self.observacion}, promedio: {self.promedio}")
    def promedio(self):
        promedio = puntualidad+productividad+equipo/3
        return promedio

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
            puntualidad = input("Puntualidad: ")
            productividad = input("Productividad: ")
            observacion = input("Observacion: ")
            equipo = input("Equipo: ")
            telefono = input("Telefono: ")
            correo = input("Correo: ")
            empleado = {
                "codigo": {
                    "nombre": nombre,
                    "departamento": departamento,
                    "antiguedad": antiguedad,
                    "evaluacion":{
                        "puntualidad": puntualidad,
                        "equipo": equipo,
                        "productividad": productividad,
                        "observacion": observacion,
                        "promedio": {},
                        "estado": {}
                    }
                },
                "contacto":{
                    "telefono": telefono,
                    "correo": correo
                }
            }
            empleados[codigo] = empleado
            empleados[codigo].promedio()
    elif opcion == 2:
        print("Informacion Empleado")





