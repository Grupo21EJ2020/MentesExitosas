class Video:
    def __init__(self, IdVideo, Nombre, url, FechaPublicacion):
        self.IdVideo = IdVideo
        self.Nombre = Nombre
        self.url = url
        self.FechaPublicacion = FechaPublicacion
    
    @property 
    def IdVideo (self):
        return self.__IdVideo
    
    @property
    def Nombre (self):
        return self.__Nombre
    
    @Nombre.setter
    def Nombre (self, valor):
        self.__Nombre = valor

    @property
    def url (self):
        return self.__url
    
    @url.setter
    def url (self, valor):
        self.__url = valor
    

