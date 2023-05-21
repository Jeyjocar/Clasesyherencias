"""
Clases y Herencias
POO
31-01-2023
"""


class Persona():
    def __init__(self, nombre, edad, pais):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais

    def presentacion(self):
        print(f'Mi nombre es {self.nombre}, mi edad es {self.edad}, soy del país de {self.pais}')


class Empleado(Persona):
    def __init__(self,sueldo, cargo, nombre_empleado, edad_empleado, pais_empleado):
        super().__init__(nombre_empleado, edad_empleado, pais_empleado)
        self.sueldo = sueldo
        self.cargo = cargo
    def presentacion(self):
        super().presentacion() #super es una clase que sirve para ayudar a las herencias
        print("salario", self.sueldo, "Cargo", self.cargo)


#empleados = Persona("Fabio", 34, "Francia")
empleados = Empleado(10000000, "Ingeniero", "Joan Manuel", 19, "años", "Colombia")
empleados.presentacion()
print(isinstance(empleados,Persona))

    




