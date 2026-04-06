from data import validate_imported, export_students 
import utils_module
#1Ingresar Estudiante
def student_insertion(students):
    new_student = {}
    try:
        name = input("Ingrese el nombre: ")
        room = input("Digite la sección: ").strip().upper()
        if utils_module.duplicated_student(name,room,students):
            raise Exception("El estudiante ya existe")
        
        spanish = float(input("Ingrese la nota de Español: "))
        english = float(input("Ingrese la nota de Inglés: "))
        social_e = float(input("Ingrese la nota de Sociales: "))
        science = float(input("Ingrese la nota de Ciencias: "))
        new_student = { "name":name,
                        "room":room,
                        "grades" : {"spanish": spanish,
                                    "english": english,
                                    "social_studies": social_e,
                                    "science": science}}
        if not utils_module.validate_student(new_student):
            raise Exception ("Hubo errores al validar los datos del estudiante")
        students.append(new_student) #append despues de la validación para asegurar ingreso de datos congruentes.
    except Exception as e:
        print(f"Error en ingreso de datos: {e}\nEl estudiante no se añadió")
    
def print_list(p_list):
    for item in p_list:
        for key, value in item.items():
            if isinstance(value,dict):
                for k, v in value.items():
                    print(f"\t{k}: {v}")
            else:        
                print(f"{key}: {value}")
#2"Listar Estudiante
def list_students(students):
    print_list(students)

#Promedio de las notas de un estudiante
def student_average_grade(student):
    try:
        grades = student["grades"].values()
        
        if len(grades) == 0:
            raise ValueError("El estudiante no tiene notas")
        
        return sum(grades) / len(grades)
    
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
        if student["room"].lower() == room and student["name"].lower() == name:
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
        reproved = False
        temp_student = {"name" : item["name"],
                        "room" : item["room"]}
        grades = {}
        for grade,valu in item["grades"].items():
            if float(valu) < 60:
                grades[grade] = valu
                reproved = True
        temp_student["grades"] = grades
        if reproved:
            reproved_students.append(temp_student)        
    if not reproved_students:
        print(f"No hay estudiantes reprobados")
        return students
    print_list(reproved_students)
