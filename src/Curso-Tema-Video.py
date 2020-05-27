from ClaseVideo import Video
objetovideo = Video() 
class CursoTemaVideo:
    def _init_(self, IdCursoTemaVideo, IdCursotema, IdVideo):
        self.__IdCursoTemaVideo = IdCursoTemaVideo
        self.__IdCursotema = IdCursotema
        self.__IdVideo = IdVideo
    
    @property 
    def IdCursoTemaVideo (self):
        return self.__IdAdministracionvideo 
    
    @IdCursoTemaVideo.setter
    def IdCursoTemaVideo (self, valor):
        self.__IdCursoTemaVideo = valor
    
    @property 
    def IdCursotema (self):
        return self.__IdCursotema 
    
    @IdCursotema.setter
    def IdCursotema (self, valor):
        self.__IdCursotema = valor

    @property 
    def IdVideo (self):
        return self.__IdVideo 
    
    @IdVideo.setter
    def IdVideo (self, valor):
        self.__IdVideo = valor


    def agregarCursoTemaVideo (self):
        archivo = open("CursoTemaVideo", "a")
        archivo.write(self.__IdCursoTemaVideo + "|" + IdCursotema + "|" + objetovideo.IdVideo + "\n")
        archivo.close()

    

    
    
   





