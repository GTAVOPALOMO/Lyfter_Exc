students = [] #Se guarda en global para usar memoria, lo ideal es guardar en BD o en archivo

def validate_student(new_student):
    KEYS = ["name", "room", "grades"]
    is_valid = True
    print("Validando estudiante ingresado..............")
    #Se valida estructura del diccionario
    if not isinstance(new_student,dict):
        print(f"Error en la estructura del estudiante")
        is_valid = False
    #Se validan las llaves del diccionario que sean exactas
    required_keys = set(KEYS)
    if set(new_student.keys()) != required_keys:
        print("Error: faltan campos o hay campos inválidos en el estudiante")
        is_valid = False

    #Validacion del nombre para solo texto
    if not isinstance(new_student[KEYS[0]], str):
        print("Error: el nombre debe ser texto")
        is_valid = False

    #Validacion de nombre vacio
    if new_student[KEYS[0]].strip() == "":
        print("Error: el nombre no debe ser vacío")
        is_valid = False

    if not isinstance(new_student[KEYS[1]], str):
        print("Error: la sección debe ser texto")
        return False

    if new_student[KEYS[1]].strip() == "":
        print("Error: la sección no debe ser vacía")
        is_valid = False

    print("Estudiante válido!!!!")
    return is_valid

#1Ingresar Estudiante
def student_insertion():
    new_student = {}
    success_insertion = False
    mistake = False
    while not success_insertion:
        try:
            name = input("Ingrese el nombre: ")
            room = input("Ingrese la sección: ")
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
        except Exception as e:
            print(f"Error en ingreso de datos: {e}")
            mistake = True
        if not mistake and validate_student(new_student):
            success_insertion = True
        else:
            print("Debido a los errores de inserción debe ingresar otra vez el estudiante.")
        students.append(new_student)

    students.append(new_student)

#2"Listar Estudiante
def list_students():
    for item in students:
        for key, value in item.items():
            if isinstance(value,dict):
                for k, v in value.items():
                    print(f"\t{k}: {v}")
            else:        
                print(f"{key}: {value}")
#3"Mejores Promedios
def best_grades():
    None
#4"Nota Promedio
def average_grade():
    None
#5"Exportar información
def export_data():
    None
#6"Importar información
def import_data():
    None

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