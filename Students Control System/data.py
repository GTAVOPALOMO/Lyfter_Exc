import csv
V_PATH = "Students Control System/students.csv"
#Parseamos el dict para aplanarlo y adecuarlo al dictwriter
def flat_students(students):
    flat_students = []
    for student in students:
        flat_student = {
            "name": student["name"],
            "room": student["room"],
            **student["grades"] #Recordar este shortcut, doble * para dicts y * para tuplas y listas
        }
        flat_students.append(flat_student)
    return flat_students
def unflat_student(student):
    unflat_student = {"name": student["name"],
                    "room": student["room"],
                    "grades": { "spanish": student["spanish"],
                                "english": student["english"],
                                "social_studies": student["social_studies"],
                                "science": student["science"]}
                    }
    return unflat_student

def export_students(students):
    if not students:
        print("No hay estudiantes para exportar")
        return
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
            students = [unflat_student(student) for student in reader]
        if not students:
            print("El archivo está vacío.")
            return    
        return students
    except FileNotFoundError:
        print("No exportó previamente o borró el archivo")
        return