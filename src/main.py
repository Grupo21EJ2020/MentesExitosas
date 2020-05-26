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
            claveCurso = int(input("Ingresa el id del curso que quieres borrar: "))
            claveCurso.eliminarCurso()

        elif submenuCurso == 4:
            archivo = open("cursos.txt","r")
            for renglon in archivo:
                print(f"Datos del renglon: {renglon}")
            archivo.close()
        
            
main()