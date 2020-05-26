class Curso():
    def __init__(self, idcurso, nombre, descripcion, idEmpleado):
        self.__idcurso = idcurso
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__idempleado = idEmpleado

    @property
    def idcurso(self):
        return self.__idcurso

    @idcurso.setter
    def idcurso(self,other):
        self.__idcurso = other

    