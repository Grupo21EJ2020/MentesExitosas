from curso import Curso
def main():
    menuInicial = int(input("1) Empleados\n2) Cursos\n3) Temas\n4) Videos\n5) Temas Asignados\n6) Administracion de Videos\nRespuesta:  "))
    if menuInicial == 2:
        submenuCurso = int(input("1) Agregar\n2) Borrar\n3) Modificar\n 4) Consultar"))
        if submenuCurso == 1:
            idCurso = str(input("Cual es el id del curso?  "))
            nombre = str(input("Cual es el nombre del curso?  "))
            descripcion = str(input("Cual es la descripcion del curso?\n"))
            idEmpleado = str(input("Cual es el id del Empleado?  "))
            cursoNuevo = Curso(idCurso,nombre,descripcion,idEmpleado)
            print(cursoNuevo)
            cursoNuevo.agregarCurso()
main()