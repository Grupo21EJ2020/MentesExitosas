class Tema:
    def __init__(self, idTema,Nombre):
        self.__idTema=idTema
        self.__Nombre=Nombre

    @property
    def idTema(self):
        return self.__idTema

    @property
    def Nombre(self):
        return self.__Nombre

    @Nombre.setter
    def Nombre(self,valor):
        self.__Nombre=valor