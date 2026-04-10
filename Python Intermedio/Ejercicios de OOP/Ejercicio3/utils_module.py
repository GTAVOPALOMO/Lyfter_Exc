#Se crea un modulo para utilidades y evitar circular imports
import re #expresiones regulares
from students import Student

KEYS = ["name", "room", "grades"]

def choice_selector(text):
    options = {"Y" : True, "N" : False}
    return bool(options.get(input(text).upper(),False))

def validate_student(new_student):
    
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
        is_valid = False
    #Validacion de sección en base a una expresión regular que acepte 1 o dos numeros y una letra mayuscula
    pattern = r"^\d{1,2}[A-Z]$" #r es para que no interprete el \ como carqcter especial de python
    print("Validando patrón de sección...")
    if not bool(re.match(pattern,new_student[KEYS[1]])):
        print("Error, debe respetar el formato NUMERO LETRA ej: 10A, 11B")
        is_valid = False
    print("Validando notas...")
    try:
        for ke,va in new_student[KEYS[2]].items():
            if float(va) > 100 or float(va) < 0:
                print(f"Error: La nota de {ke} presenta una anomalía, favor revisar")
                is_valid = False
            else:
                new_student[KEYS[2]][ke] = float(va)
    except Exception as e:
        print(f"Error validando las notas: {e}")
        is_valid = False
    print("Estudiante válido!!!!")
    return is_valid

def student_to_dict(student: Student):
    student_JSON = {}
    student_JSON[KEYS[0]] = student.name
    student_JSON[KEYS[1]] = student.room
    student_JSON[KEYS[2]] = {"spanish": student.g_spanish,
                                "english": student.g_english,
                                "social_studies": student.g_social_studies,
                                "science": student.g_science}
    return student_JSON


def duplicated_student(name,room,students):
    for student in students:
        print(f"validando a {student.name.lower()}")
        if student.name.lower() == name.lower() and student.room.lower() == room.lower():
            print(f"Ya el estudiante {name} existe en la sección {room}")
            return True
    return False