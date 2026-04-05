from data import import_students, export_students 
import re #expresiones regulares

students = [] #Se guarda en global para usar memoria, lo ideal es guardar en BD o en archivo

def choice_selector(text):
    options = {"Y" : True, "N" : False}
    return bool(options.get(input(text).upper(),False))

def validate_student(new_student):
    KEYS = ["name", "room", "grades"]
    is_valid = True
    print("Validando estudiante ingresado..............")
    print("Validando dict...")
    #Se valida estructura del diccionario
    if not isinstance(new_student,dict):
        print(f"Error en la estructura del estudiante")
        is_valid = False
    print("Validando llaves...")
    #Se validan las llaves del diccionario que sean exactas
    required_keys = set(KEYS)
    if set(new_student.keys()) != required_keys:
        print("Error: faltan campos o hay campos inválidos en el estudiante")
        is_valid = False
    print("Validando nombre vacio...")
    #Validacion de nombre vacio
    if new_student[KEYS[0]].strip() == "":
        print("Error: el nombre no debe ser vacío")
        is_valid = False
    print("Validando nombre textual...")
    #Validacion del nombre para solo texto
    if not new_student[KEYS[0]].replace(" ", "").isalpha(): #si no es alpha(alfabético) revienta
        print("Error: el nombre debe ser solo texto")
        is_valid = False
    print("Validando sección vacia...")
    if new_student[KEYS[1]].strip() == "":
        print("Error: la sección no debe ser vacía")
        is_valid = False
    print("Validando sección textual...")
    if new_student[KEYS[1]].isnumeric():
        print("Error: la sección debe ser texto")
        return False
    #Validacion de sección en base a una expresión regular que acepte 1 o dos numeros y una letra mayuscula
    pattern = r"^\d{1,2}[A-Z]$" #r es para que no interprete el \ como carqcter especial de python
    print("Validando patrón de sección...")
    if not bool(re.match(pattern,new_student[KEYS[1]])):
        return False
    print("Validando notas...")
    for ke,va in new_student[KEYS[2]].items():
        if float(va) > 100 or float(va) < 0:
            print(f"Error: La nota de {ke} presenta una anomalía, favor revisar")
            is_valid = False
            
    print("Estudiante válido!!!!")
    return is_valid

def duplicated_student(name,room):
    for student in students:
        if student["name"].lower() == name.lower() and student["room"].lower() == room.lower():
            print(f"validando a {student["name"].lower()}")
            print(f"Ya el estudiante {name} existe en la sección {room}")
            return True
    return False

#1Ingresar Estudiante
def student_insertion():
    new_student = {}
    try:
        name = input("Ingrese el nombre: ")
        room = input("Digite la sección: ").strip().upper()
        if duplicated_student(name,room):
            raise Exception("El estudiante ya existe")
        
        spanish = float(input("Ingrese la nota de Español: "))
        english = float(input("Ingrese la nota de Inglés: "))
        social_e = float(input("Ingrese la nota de Estudios Sociales: "))
        science = float(input("Ingrese la nota de Ciencias: "))
        new_student = { "name":name,
                        "room":room,
                        "grades" : {"spanish": spanish,
                                    "english": english,
                                    "social_studies": social_e,
                                    "science": science}}
        if not validate_student(new_student):
            raise Exception ("Hubo errores al validar los datos del estudiante")
    except Exception as e:
        print(f"Error en ingreso de datos: {e}\nEl estudiante no se añadió")
    students.append(new_student)

def print_list(p_list):
    for item in p_list:
        for key, value in item.items():
            if isinstance(value,dict):
                for k, v in value.items():
                    print(f"\t{k}: {v}")
            else:        
                print(f"{key}: {value}")
#2"Listar Estudiante
def list_students():
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
def best_grades():
    top_students = sorted(students, key=student_average_grade, reverse=True)
    print_list(top_students[:3])

#4"Nota Promedio
def average_grade():
    average = []
    for student in students:
        average.append(student_average_grade(student))
    print(f"El promedio de las notas de los estudiantes es: {sum(average)/len(average)}")
#5"Exportar información
def export_data():
    export_students(students)
#6"Importar información
def import_data():
    temp_students = import_students()
    for item in temp_students:
        if not validate_student(item):
            print(f"Error en la carga de archivos con el estudiante {item}")
        else:
            students.append(item)
    print(f"Carga completada")
#7 Remover estudiante
def remove_student():
    name = input("Digite el nombre del estudiante: ").lower()
    room = input("Digite la sección: ").lower()
    deleted = False #En caso de duplicados que borre todos
    for i, student in enumerate(students):
        if student["room"].lower() == room and student["name"].lower() == name:
            if choice_selector(f"Desea eliminar a {name} de la sección {room} [Y/N]: "):
                students.pop(i)
                print("Estudiante eliminado")
                deleted = True
    if deleted:
        return
    print("Estudiante no encontrado")   

def list_reproved():
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
        return
    print_list(reproved_students)
#Procesar opción seleccionada
def process_choice(choice):
    if choice == 1:
        student_insertion()
    if choice == 2:
        list_students()
    if choice == 3:
        best_grades()
    if choice == 4:
        average_grade()
    if choice == 5:
        export_data()
    if choice == 6:
        import_data()
    if choice == 7:
        remove_student()
    if choice == 8:
        list_reproved()