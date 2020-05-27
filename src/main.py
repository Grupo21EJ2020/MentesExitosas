from os import system, name
from curso import Curso
from ClaseVideo import Video
from Tema import Tema

def borrar():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def main():
    menuInicial = 0
    while menuInicial != 7:
        menuInicial = int(input("1) Empleados\n2) Cursos\n3) Temas\n4) Videos\n5) Temas Asignados\n6) Administracion de Videos\n7) Salir\nRespuesta:  "))
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
                input("Presione enter para continuar...")
                borrar()
            elif submenuCurso == 2:
                idCurso = str(input("Digita el id del curso que quieres borrar:  "))
                ListaCursos = []
                archivo = open("./archivos/cursos.txt", "r")
                for n in archivo:
                    ListaCursos.append(n)
                    if idCurso == n[0]:
                        ListaCursos.remove(n)
                    archivo2 = open("./archivos/cursos2.txt","w")
                    for g in ListaCursos:
                        archivo2.write(g)
                    archivo2.close()
                archivo.close()
                archivoorigen = open("./archivos/cursos2.txt","r")
                archivodestino = open("./archivos/cursos.txt","w")
                archivodestino.write(archivoorigen.read())
                archivoorigen.close()
                archivodestino.close()
                input("Presione enter para continuar...")
                borrar()
            elif submenuCurso == 3:
                idCurso = str(input("Digita el id del curso que quieres modificar:  "))
                ListaCursos = []
                archivo = open("./archivos/cursos.txt")
                for n in archivo:
                    ListaCursos.append(n)
                    if idCurso == n[0]:
                        nombreN = str(input("Digite el Nombre de curso nuevo:  "))
                        descripcionN = str(input("Digite la descripcion de curso nueva:\n  "))
                        idEmpleadoN = str(input("Digite el id de empleado nuevo:  "))
                        C = idCurso + " | " + nombreN + " | " + descripcionN + " | " + idEmpleadoN + "\n"
                        ListaCursos.remove(n)
                        ListaCursos.append(C)
                    archivo2 = open("./archivos/cursos2.txt","w")
                    for x in ListaCursos:
                        archivo2.write(x)
                    archivo2.close()
                archivo.close()
                archivoorigen = open("./archivos/cursos2.txt","r")
                archivodestino = open("./archivos/cursos.txt","w")
                archivodestino.write(archivoorigen.read())
                archivoorigen.close()
                archivodestino.close()
            elif submenuCurso == 4:
                borrar()
                print("Lista de Cursos\n")
                archivo = open("./archivos/cursos.txt","r")
                for renglon in archivo:
                    print(f"Datos del renglon: {renglon}")
                archivo.close()
                input("Presione enter para continuar...")
                borrar()

        if menuInicial == 3:
            submenuTema = int(input("1) Agregar\n2) Borrar\n3) Modificar\n4) Consultar\nRespuesta:  "))
            if submenuTema== 1:
                idTema = str(input("Cual es el id del tema?  "))
                Nombre = str(input("Cual es el nombre del tema?  "))
                temaNuevo = Tema(idTema,Nombre)
                print(temaNuevo)
                temaNuevo.agregarTema()
            elif submenuTema == 2:
                idTema  = str(input("Digita el id del tema que quieres borrar:  "))
                ListaTemas = []
                archivoTema = open("./archivos/Temas.txt", "r")
                for n in archivoTema:
                    ListaTemas.append(n)
                    if idTema== n[0]:
                        ListaTemas.remove(n)
                    archivoTema2 = open("./archivos/Temas2.txt","w")
                    for g in ListaTemas:
                        archivoTema2.write(g)
                    archivoTema2.close()
                archivoTema.close()
                archivoorigen = open("./archivos/Temas2.txt","r")
                archivodestino = open("./archivos/Temas.txt","w")
                archivodestino.write(archivoorigen.read())
                archivoorigen.close()
                archivodestino.close()
                
            elif submenuTema == 4:
                archivoTema = open("./archivos/Temas.txt","r")
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
            
            if submenuVideo == 2:
                IdVideo = (input("Dime el ID del Video que quieras borrar: "))
                ListaVideo = []
                archivoVideo = open("./archivos/ClaseVideo.txt","w")
                for n in archivoVideo:
                    ListaVideo.append(n)
                    if IdVideo == n[0]:
                        ListaVideo.remove(n)
                    archivoVideo2 = open ("./archivos/ClaseVideo2.txt", "w")
                    for g in ListaVideo:
                        archivoVideo2.write(g)
                    archivoVideo2.close()
                archivoVideo.close()
                archivoorigen = open("./archivos/ClaseVideo2.txt","r")
                archivodestino = open("./archivos/ClaseVideo.txt","w")
                archivodestino.write(archivoorigen.read())
                archivoorigen.close()
                archivodestino.close()
            
            elif submenuVideo == 4:
                archivoVideo = open("./archivos/ClaseVideo.txt","r")
                for renglon in archivoVideo:
                    print(f'Datos del Video: {renglon}')
                archivoVideo.close()
main()