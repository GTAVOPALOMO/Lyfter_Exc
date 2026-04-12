from data import validate_imported, export_students 
from students import Student
import utils_module
#1Ingresar Estudiante
def student_insertion(students):
    try:
        name = input("Ingrese el nombre: ")
        room = input("Digite la sección: ").strip().upper()
        if utils_module.duplicated_student(name,room,students):
            raise Exception("El estudiante ya existe")
        
        spanish = float(input("Ingrese la nota de Español: "))
        english = float(input("Ingrese la nota de Inglés: "))
        social_e = float(input("Ingrese la nota de Sociales: "))
        science = float(input("Ingrese la nota de Ciencias: "))
        new_student = Student(name,room,spanish,english,social_e,science)
        if not utils_module.validate_student(utils_module.student_to_dict(new_student)):
            raise Exception ("Hubo errores al validar los datos del estudiante")
        students.append(new_student) #append despues de la validación para asegurar ingreso de datos congruentes.
    except Exception as e:
        print(f"Error en ingreso de datos: {e}\nEl estudiante no se añadió")
    
def print_list(p_list):
    for item in p_list:
        item.print_info()
#2"Listar Estudiante
def list_students(students):
    print_list(students)

#Promedio de las notas de un estudiante
def student_average_grade(student: Student):
    try:
        grades = [student.g_spanish,student.g_english,student.g_social_studies,student.g_science]
        numeric_grades = [float(grade) for grade in grades]
        return sum(numeric_grades) / len(numeric_grades)
    except Exception as e:
        print(f"ERROR CALCULANDO EL PROMEDIO: {e}")
        return -1

#3"Mejores Promedios
def best_grades(students):
    top_students = sorted(students, key=student_average_grade, reverse=True)
    print_list(top_students[:3])

#4"Nota Promedio
def average_grade(students):
    average = []
    for student in students:
        average.append(student_average_grade(student))
    print(f"El promedio de las notas de los estudiantes es: {sum(average)/len(average)}")

#7 Remover estudiante
def remove_student(students):
    name = input("Digite el nombre del estudiante: ").lower()
    room = input("Digite la sección: ").lower()
    deleted = False #En caso de duplicados que borre todos
    for i, student in enumerate(students):
        if student.room.lower() == room and student.name.lower() == name:
            if utils_module.choice_selector(f"Desea eliminar a {name} de la sección {room} [Y/N]: "):
                students.pop(i)
                print("Estudiante eliminado")
                deleted = True
    if deleted:
        return students
    print("Estudiante no encontrado")   

def list_reproved(students):
    reproved_students = []
    for item in students:
        if float(item.g_spanish) < 60  or float(item.g_english) < 60 or float(item.g_social_studies) < 60 or float(item.g_science) < 60:
            reproved_students.append(item)        
    if not reproved_students:
        print(f"No hay estudiantes reprobados")
        return students
    print_list(reproved_students)
