class Curso():
    def __init__(self, idCurso, nombre, descripcion, idEmpleado):
        self.__idCurso = idCurso
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__idEmpleado = idEmpleado

    @property
    def idCurso(self):
        return self.__idCurso

    @idCurso.setter
    def idCurso(self,other):
        self.__idCurso = other

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,other):
        self.__nombre = other

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self,other):
        self.__descripcion = other

    @property
    def idEmpleado(self):
        return self.__idEmpleado

    @idEmpleado.setter
    def idEmpleado(self,other):
        self.__idEmpleado = other

    def __str__(self):
        return f"El id del curso es: {self.__idCurso}\nEl nombre del curso es: {self.__nombre}\nLa descripcion del curso es: {self.__descripcion}\nEl id del Empleado es {self.__idEmpleado}"
    
    def agregarCurso(self):
        archivo = open("cursos.txt","a")
        archivo.write(self.__idCurso + "|" + self.__nombre + "|" + self.__descripcion + "|" + self.__idEmpleado + "\n")
        archivo.close()

    def eliminarCurso(self, claveCurso):
        Lista = []
        archivo = open("cursos.txt")
        for n in archivo:
            Lista.append(n)
            if clave == n[0]:
                Lista.remove(n)
            archivo2 = open(archivo,"w")
            for g in Lista:
                archivo2.write(g)
            archivo2.close()
        archivo.close()

