from actions import process_choice

OPTIONS = [ "Salir",
            "Ingresar Estudiante",
            "Listar Estudiante",
            "Mejores Promedios",
            "Nota Promedio",
            "Exportar información",
            "Importar información"]

def start():
    choice = 1
    while choice != 0:
        
        try:
            choice = option_choice()
            if choice < 0:
                raise ValueError("Valor negativo")
            if choice >= len(OPTIONS):
                raise ValueError("Valor no existente")
        except ValueError as e:
            print(f"******ERROR******\nOPCION NO VALIDA\n{e}\n******ERROR******\n")
        if(choice != 0):
            process_choice(choice)


def option_choice():
    print("Bienvenido al sistema de control de estudiantes")
    for i, item in enumerate(OPTIONS):
        if i == 0:
            continue
        print(f"[{i}] - {item.upper()}")
    print(f"[0] - {OPTIONS[0]}")
    return int(input("Seleccione una opción: "))