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

    def ConsultarInfo(self):
        print(f"{'Id Tema' :<10}{'Nombre':<20}")
        print(f"{self.__idTema: <10}{self.__Nombre}")

    def agregarTema(self):
        archivo = open("Temas.txt","a")
        archivo.write(self.__idTema + "|" + self.__Nombre + "\n")
        archivo.close()