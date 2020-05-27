from ClaseVideo import Video
from curso_tema import Curso_Tema
class Curso_Tema_Video():
    def __init__(self, idCursoTemaVideo, idCursoTema, IdVideo):
        self.__idCursoTemaVideo = idCursoTemaVideo
        self.__idCursoTema = idCursoTema
        self.__IdVideo = IdVideo

    @property 
    def idCursoTemaVideo (self):
        return self.__idCursoTemaVideo 
    
    @idCursoTemaVideo.setter
    def idCursoTemaVideo (self, valor):
        self.__idCursoTemaVideo = valor
    
    def __str__(self):
        return f"{self.__idCursoTemaVideo}\n{self.__idCursoTema}\n{self.__IdVideo}"
        
    def agregarCursoTemaVideo (self):
        archivo = open("./archivos/curso_tema_video.txt", "a")
        archivo.write(self.__idCursoTemaVideo + "|" + self.__idCursoTema + "|" + self.__IdVideo + "\n")
        archivo.close()

    

    
    
   





