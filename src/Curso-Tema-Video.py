class Administracionvideo:
    def _init_(self, IdAdministracionvideo, IdCursotema, IdVideo):
        self.__IdAdministracionvideo = IdAdministracionvideo
        self.__IdCursotema = IdCursotema
        self.__IdVideo = IdVideo
    
    @property 
    def IdAdministracionvideo (self):
        return self.__IdAdministracionvideo 
    
    @IdAdministracionvideo.setter
    def IdAdministracionvideo (self, valor):
        self.__IdAdministracionvideo = valor
    
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
    
   





