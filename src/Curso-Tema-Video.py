from ClaseVideo import Video
objetovideo = Video() 
class CursoTemaVideo:
    def _init_(self, IdCursoTemaVideo):
        self.__IdCursoTemaVideo = IdCursoTemaVideo
    
    @property 
    def IdCursoTemaVideo (self):
        return self.__IdAdministracionvideo 
    
    @IdCursoTemaVideo.setter
    def IdCursoTemaVideo (self, valor):
        self.__IdCursoTemaVideo = valor

    def agregarCursoTemaVideo (self):
        archivo = open("CursoTemaVideo", "a")
        archivo.write(self.__IdCursoTemaVideo + "|" + IdCursotema + "|" + objetovideo.IdVideo + "\n")
        archivo.close()

    

    
    
   





