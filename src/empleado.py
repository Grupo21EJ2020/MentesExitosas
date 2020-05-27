class Empleado():
    def __init__(self, idEmpleado, nombre, direccion):
        self.__idEmpleado = idEmpleado
        self.__nombre = nombre
        self.__direccion = direccion

    @property
    def idEmpleado(self):
        return self.__idEmpleado

    @idEmpleado.setter
    def idEmpleado(self,other):
        self.__idEmpleado = other
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,other):
        self.__nombre = other

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self,other):
        self.__direccion = other

    def __str__(self):
        return f"El id del empleado es: {self.__idEmpleado}\nEl nombre del empleado es: {self.__nombre}\nLa direccion del empleado es: {self.__direccion}"

    def agregarEmpleado(self):
        archivo = open("./archivos/empleados.txt","a")
        archivo.write(self.__idEmpleado + " | " + self.__nombre + " | " + self.__direccion + "\n")
        archivo.close()
