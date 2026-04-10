import actions
import data

OPTIONS = [ "Salir",
            "Ingresar Estudiante",
            "Listar Estudiante",
            "Mejores Promedios",
            "Nota Promedio",
            "Exportar información",
            "Importar información",
            "Borrar estudiante",
            "Mostar reprobados"]

def start(students):
    choice = 1
    while choice != 0:
        
        try:
            choice = option_choice()
            if choice < 0:
                raise ValueError("Valor negativo")
            if choice >= len(OPTIONS):
                raise ValueError("Valor no existente")
            if(choice != 0):
                process_choice(choice,students)
        except ValueError as e:
            print(f"******ERROR******\nOPCION NO VALIDA\n{e}\n******ERROR******\n")

#Procesar opción seleccionada
def process_choice(choice,students):
    if choice == 1:
        actions.student_insertion(students)
    if choice == 2:
        actions.list_students(students)
    if choice == 3:
        actions.best_grades(students)
    if choice == 4:
        actions.average_grade(students)
    if choice == 5:
        data.export_students(students) #Importado desde data
    if choice == 6:
        data.validate_imported(students)
    if choice == 7:
        actions.remove_student(students)
    if choice == 8:
        actions.list_reproved(students)

def option_choice():
    print("Bienvenido al sistema de control de estudiantes")
    for i, item in enumerate(OPTIONS):
        if i == 0:
            continue
        print(f"[{i}] - {item.upper()}")
    print(f"[0] - {OPTIONS[0]}")
    return int(input("Seleccione una opción: "))