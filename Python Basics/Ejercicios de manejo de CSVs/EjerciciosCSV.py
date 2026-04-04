import csv
def game_info_collector(p_path):
    games = []
    choice = "y"
    while choice == "y":
        temp_dict = {}
        temp_name = input("Ingrese el nombre: ")
        temp_gen = input("Ingrese el genero: ")
        temp_dev = input("Ingrese el desarrollador: ")
        temp_ESRB = input("Ingrese clasificacion: ")
        temp_dict["Name"] = temp_name
        temp_dict["Genre"] = temp_gen
        temp_dict["Developer"] = temp_dev
        temp_dict["ESRB"] = temp_ESRB
        games.append(temp_dict)
        choice = input("Desea agregar mas juegos? Y/N").lower()
    with open(p_path, "w", newline="", encoding="utf-8") as new_file: #se agrega el newline proque csv agrega saltos de linea tambien
        writer = csv.DictWriter(new_file, games[0].keys())
        writer.writeheader()
        writer.writerows(games)

game_info_collector("csv_test.csv")

def game_info_collector_tab(p_path):
    games = []
    choice = "y"
    while choice == "y":
        temp_dict = {}
        temp_name = input("Ingrese el nombre: ")
        temp_gen = input("Ingrese el genero: ")
        temp_dev = input("Ingrese el desarrollador: ")
        temp_ESRB = input("Ingrese clasificacion: ")
        temp_dict["Name"] = temp_name
        temp_dict["Genre"] = temp_gen
        temp_dict["Developer"] = temp_dev
        temp_dict["ESRB"] = temp_ESRB
        games.append(temp_dict)
        choice = input("Desea agregar mas juegos? Y/N").lower()
    with open(p_path, "w", newline="", encoding="utf-8") as new_file: #se agrega el newline proque csv agrega saltos de linea tambien
        writer = csv.DictWriter(new_file, games[0].keys(), delimiter="\t") #cambiando el delimiter a \t se cambia el separador de coma a tabulación
        writer.writeheader()
        writer.writerows(games)

game_info_collector_tab("csv_test_tab.csv")
