from ClaseVideo import Video
from Curso_tema import Curso_Tema
class CursoTemaVideo:
    def _init_(self, idCursoTemaVideo, idCursoTema, IdVideo):
        self.__idCursoTemaVideo = idCursoTemaVideo
        self.__idCursoTema = idCursoTema
        self.__IdVideo = IdVideo

    @property 
    def idCursoTemaVideo (self):
        return self.__idCursoTemaVideo 
    
    @idCursoTemaVideo.setter
    def idCursoTemaVideo (self, valor):
        self.__idCursoTemaVideo = valor

    def agregarCursoTemaVideo (self):
        archivo = open("CursoTemaVideo", "a")
        archivo.write(self.__idCursoTemaVideo + "|" + self.__idCursoTema + "|" + self.__IdVideo + "\n")
        archivo.close()

    

    
    
   





