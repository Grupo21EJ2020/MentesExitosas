from curso import Curso
from Tema import Tema
class Curso_Tema():
    def __init__(self, idCursoTema, idCurso, idTema):
        self.__idCursoTema = idCursoTema
        self.__idCurso = idCurso
        self.__idTema = idTema

    @property
    def idCursoTema(self):
        return self.__idCursoTema

    @idCursoTema.setter
    def idCursoTema(self, other):
        self.__idCursoTema = other

    def __str__(self):
        return f"El id de Curso del Tema es:  {self.__idCursoTema}\nEl id del Curso es:  {self.__idCurso}\nEl id del Tema es:  {self.__idTema}"

    def agregarCursoTema(self):
        archivo = open("curso_tema.txt","a")
        archivo.write(self.__idCursoTema + " | " + self.__idCurso + " | " + self.__idTema + "\n")
        archivo.close()