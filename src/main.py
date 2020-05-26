from curso import Curso
from ClaseVideo import Video
from tema import Tema
def main():
    menuInicial = int(input("1) Empleados\n2) Cursos\n3) Temas\n4) Videos\n5) Temas Asignados\n6) Administracion de Videos\nRespuesta:  "))
    if menuInicial == 2:
        submenuCurso = int(input("1) Agregar\n2) Borrar\n3) Modificar\n4) Consultar\nRespuesta:  "))
        if submenuCurso == 1:
            idCurso = str(input("Cual es el id del curso?  "))
            nombre = str(input("Cual es el nombre del curso?  "))
            descripcion = str(input("Cual es la descripcion del curso?\n"))
            idEmpleado = str(input("Cual es el id del Empleado?  "))
            cursoNuevo = Curso(idCurso,nombre,descripcion,idEmpleado)
            print(cursoNuevo)
            cursoNuevo.agregarCurso()
    if menuInicial == 3:
        submenuTema = int(input("1) Agregar\n2) Borrar\n3) Modificar\n4) Consultar\nRespuesta:  "))
        if submenuTema== 1:
            idTema = str(input("Cual es el id del tema?  "))
            Nombre = str(input("Cual es el nombre del tema?  "))
            temaNuevo = Tema(idTema,Nombre)
            print(temaNuevo)
            temaNuevo.agregarTema()
    if menuInicial == 4:
        menuVideo = int(input("1) Agregar\n 2)Borrar\n 3)Modificar\n 4)Consultar"))
        if menuVideo == 1:
            IdVideo = int(input("Cual es el ID del Video: "))
            Nombre = str (input("Cual es el nombre del Video: "))
            url = str (input ("Cual es la URL del Video: "))
            FechaPublicacion = (input ("Cual es la Fecha de Publicacion del Video: "))
            VideoNuevo = Video( IdVideo, Nombre, url, FechaPublicacion)
            print(VideoNuevo)
            nuevoVideo.agregarVideo()


                   
main()