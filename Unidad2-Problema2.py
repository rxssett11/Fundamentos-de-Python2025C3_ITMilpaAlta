"""
ROSETE ZEPEDA ISMAEL
Sistema de evaluación
En una escuela se quiere crear un sistema de evaluación para profesores que permita la obtención de los alumnos aprobados y reprobados de acuerdo a su historial académico, dicho sistema ayudará a dar de forma rápida todos los datos del alumno, siguiendo las siguientes condiciones:
•	Deberá pedir el número de alumnos y materias, pedir el nombre del alumno, y su matrícula.
•	El sistema debe evaluar, como condición de evaluación, qué si es una calificación mayor a 6, es aprobado y de lo contrario, reprobado. 
•	Validar que no se puede dejar información en blanco o campos vacíos.

"""

# Pedimos el número total de estudiantes y materias.
numeroEstudiantes = int(input("Ingrese el número total de alumnos: "))
numeroMaterias = int(input("Ingrese el número de materias por alumno: "))

# Creamos una lista vacía que guardará los datos de todos los estudiantes.
estudiantesDatos = []

# Este bucle recorre a cada estudiante.
for i in range(numeroEstudiantes):
    print(f"\nDatos del alumno {i + 1}")
    nombreEstudiante = input("Nombre del alumno: ")
    numeroControl = input("Matrícula del alumno: ")

    # Creamos una lista para las calificaciones del estudiante actual.
    calificacionesEstudiantes = []
    
    # Este bucle pide las calificaciones para cada materia.
    for j in range(numeroMaterias):
        # Usamos un bucle 'while' para asegurar que se ingrese una calificación válida.
        while True:
            try:
                # Pedimos la calificación y la convertimos a un número con decimales ('float').
                calificacion = float(input(f"Calificación de la materia {j + 1}: "))
                # Verificamos que la calificación esté entre 0 y 10.
                if 0 <= calificacion <= 10:
                    calificacionesEstudiantes.append(calificacion)
                    break # Si la calificación es válida, salimos del bucle.
                else:
                    print("Por favor, ingrese una calificación entre 0 y 10.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")

    # Calculamos el promedio del estudiante.
    promedioEstudiantes = sum(calificacionesEstudiantes) / numeroMaterias
    
    # Determinamos si el estudiante aprobó o no.
    status = "Aprobado" if promedioEstudiantes >= 6 else "Reprobado"
    
    # Guardamos toda la información del estudiante en un diccionario.
    student_info = {
        "nombre": nombreEstudiante,
        "matricula": numeroControl,
        "calificaciones": calificacionesEstudiantes,
        "promedio": promedioEstudiantes,
        "estado": status
    }
    
    # Agregamos el diccionario del estudiante a la lista principal.
    estudiantesDatos.append(student_info)

# Finalmente, mostramos los resultados de todos los estudiantes.
print("\nResultados de la Evaluación")
for student in estudiantesDatos:
    print("\n Información del Alumno")
    print(f"Nombre: {student['nombre']}")
    print(f"Matrícula: {student['matricula']}")
    print(f"Calificaciones: {student['calificaciones']}")
    print(f"Promedio: {student['promedio']}")
    
    # Mostramos el resultado final de Aprobado o Reprobado.
    if student['estado'] == "Aprobado":
        print(f"Resultado: ¡Aprobado!")
    else:
        print(f"Resultado: No Aprobado")
