import csv
from utils_module import validate_student
from utils_module import student_to_dict
from students import Student
V_PATH = "Python Intermedio/Ejercicios de OOP/Ejercicio3/students.csv"
#Parseamos el dict para aplanarlo y adecuarlo al dictwriter
def flat_students(students):
    flat_students = []
    for student in students:
        student = student_to_dict(student)
        flat_student = {
            "name": student["name"],
            "room": student["room"],
            **student["grades"] #Recordar este shortcut, doble * para dicts y * para tuplas y listas
        }
        flat_students.append(flat_student)
    return flat_students
def parse_to_student(student_JSON):
    parsed_student = Student(student_JSON["name"],student_JSON["room"],student_JSON["spanish"],
                            student_JSON["english"],student_JSON["social_studies"],student_JSON["science"])
    return parsed_student

def export_students(students):
    if not students:
        print("No hay estudiantes para exportar")
        return students
    parsed_students = flat_students(students)
    with open(V_PATH, "w", newline="", encoding="utf-8") as new_file:
        writer = csv.DictWriter(new_file, parsed_students[0].keys())
        writer.writeheader()
        writer.writerows(parsed_students)
def import_students():
    students = []
    try:
        with open(V_PATH, "r", encoding="utf-8", newline="") as v_file:
            reader = csv.DictReader(v_file)
            students = [parse_to_student(student) for student in reader]
        if not students:
            print("El archivo está vacío.")
        return students
    except FileNotFoundError:
        print("No exportó previamente o borró el archivo")
        return students
    
#6" Valida la información importada
def validate_imported(students):
    temp_students = import_students()
    if not temp_students:
        print(f"No hay nada que cargar...")
        return students
    for item in temp_students:
        if not validate_student(student_to_dict(item)):
            print(f"Error en la carga de archivos con el estudiante {item}")
        else:
            students.append(item)
    print(f"Carga completada")
    return students