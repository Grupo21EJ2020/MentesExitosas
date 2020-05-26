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
        elif submenuCurso == 2:
            idCurso = str(input("Digita el id del curso que quieres borrar:  "))
            ListaCursos = []
            archivo = open("cursos.txt", "r")
            for n in archivo:
                Lista.append(n)
                if id == n[0]:
                    ListaCursos.remove(n)
                archivo2 = open("cursos2.txt","w")
                for g in Lista:
                    archivo2.write(g)
                archivo2.close()
            archivo.close()
            archivoorigen = open("cursos2.txt","r")
            archivodestino = open("cursos.txt","w")
            archivodestino.write(archivoorigen.read())
            archivoorigen.close()
            archivodestino.close()
        elif submenuCurso == 4:
            archivo = open("cursos.txt","r")
            for renglon in archivo:
                print(f"Datos del renglon: {renglon}")
            archivo.close()

    if menuInicial == 3:
        submenuTema = int(input("1) Agregar\n2) Borrar\n3) Modificar\n4) Consultar\nRespuesta:  "))
        if submenuTema== 1:
            idTema = int(input("Cual es el id del tema?  "))
            Nombre = str(input("Cual es el nombre del tema?  "))
            temaNuevo = Tema(idTema,Nombre)
            print(temaNuevo)
            temaNuevo.agregarTema()
            
        elif submenuTema == 4:
            archivoTema = open("Temas.txt","r")
            for renglon in archivoTema:
                print(f"Datos del Tema: {renglon}")
            archivoTema.close()

    if menuInicial == 4:
        submenuVideo = int(input("1) Agregar\n2) Borrar\n3) Modificar\n4) Consultar : ")) 
        if submenuVideo == 1:
            IdVideo = str(input("Cual es el ID del Video: "))
            Nombre = str(input("Cual es el Nombre del Video: "))
            url = str(input("Cual es la url del Video: "))
            FechaPublicacion = str(input("Cual es la Fecha de Publicacion del Video: "))
            nuevoVideo = Video(IdVideo, Nombre, url, FechaPublicacion)  
            print(nuevoVideo)
            nuevoVideo.agregarVideo()
        
        elif submenuVideo == 4:
            archivoVideo = open("ClaseVideo.txt","r")
            for renglon in archivoVideo:
                print(f'Datos del Video: {renglon}')
            archivoVideo.close()
main()