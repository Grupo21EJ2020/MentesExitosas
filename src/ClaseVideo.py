class Video():
    def __init__(self, IdVideo, Nombre, url, FechaPublicacion):
        self.__IdVideo = IdVideo
        self.__Nombre = Nombre
        self.__url = url
        self.__FechaPublicacion = FechaPublicacion
    
    @property 
    def IdVideo (self):
        return self.__IdVideo

    @IdVideo.setter
    def IdVideo (self, valor):
        self.__IdVideo = valor
    
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
    
    @property
    def FechaPublicacion (self):
        return self.__FechaPublicacion

    @FechaPublicacion.setter 
    def FechaPublicacion (self, valor ):
        self.__FechaPublicacion = valor 
    
    def Informacion (self):
        print (f"{'ID Video' :<10}{'Nombre' :<20}{'URL' :<10}{'Fecha de Publicacion':<20}")
        print (f"{self.__IdVideo:<10}{self.__Nombre:<20}{self.__url:<10}{self.__FechaPublicacion:<20}")

    def __str__(self):
        return f"\n{self.__IdVideo}\n{self.__Nombre}\n{self.__url}\n{self.__FechaPublicacion}\n"

    def agregarVideo(self):
        archivotxt = open ('./archivos/videos.txt','a', encoding='utf8')
        archivotxt.write (self.__IdVideo + ' | ' + self.__Nombre + ' | ' + self.__url + ' | ' + self.__FechaPublicacion + '\n')
        archivotxt.close()


    

    

    
    
    

