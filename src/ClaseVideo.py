class Video:
    def __init__(self, IdVideo, Nombre, url, FechaPublicacion):
        self.__IdVideo = IdVideo
        self.__Nombre = Nombre
        self.__url = url
        self.__FechaPublicacion = FechaPublicacion
    
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
    
    @property
    def FechaPublicacion (self):
        return self.__FechaPuclicacion
    
    def Informacion (self):
        print (f"{'ID Video' :<10}{'Nombre' :<20}{'URL' :<10}{'Fecha de Publicacion':<20}")
        print (f"{self.__IdVideo:<10}{self.__Nombre:<20}{self.__url:<10}{self.__FechaPuclicacion:<20}")

    def VideoEnArchivo(self):
        archivotxt = open ('./archivos/ videos.txt','a', encoding='utf8')
        archivotxt.write (self.__IdVideo + '|' + self.__Nombre + '|'+ self.__url +'|' + self.__FechaPuclicacion  )
        archivotxt.close()

    @classmethod
    def EliminarVideo(self, archivotxt, IdVideo):
        listaVideos = []
        Archivo1 = open(archivotxt, encoding ='utf8')
        for clave in Archivo1: 
            listaVideos.append (clave) 
            if IdVideo == clave[0]:
                listaVideos.remove(n)
            OtroArchivo = open (archivotxt,'w', encoding = 'utf8')
            for g in listaVideos:
                OtroArchivo.write(g)
            OtroArchivo.close()
        Archivo1.close()

    

    

    
    
    

