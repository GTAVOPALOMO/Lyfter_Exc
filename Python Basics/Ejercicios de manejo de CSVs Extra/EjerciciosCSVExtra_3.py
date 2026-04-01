
import os 
import csv
#Valores estáticos para unificacion de mantenimiento de encabezados de archivo
HEADERS = ["Name","Genre","Developer","ESRB"]
HEAD_NAME = HEADERS[0]
HEAD_GENRE = HEADERS[1]
HEAD_DEV =  HEADERS[2]
HEAD_ESRB = HEADERS[3]

###Las validaciones para dictreader cambian.
def valid_size(p_path): #Validación de tamaño (EDGE CASE)
    MAXIMUM_SIZE = 500
    file_size = os.path.getsize(p_path)
    if file_size > MAXIMUM_SIZE: # 3 El archivo es demasiado grande
        print(f"El tamaño del archivo[{file_size}] es superior al máximo permitido[{MAXIMUM_SIZE}]")
        return False
    return True

def valid_headers(headers): 
    
    #Se valida que no esté vacío antes de otras validaciones
    if not headers:
        print("El archivo no contiene encabezados válidos.")
        return False
    normalized_headers = [h.strip().lower() for h in headers]
    expected_headers = [h.strip().lower() for h in HEADERS]
    valid_head = True
    #Alguna columna vacía
    if any(h == "" for h in normalized_headers): #Validacion de encabezados (Vacios)
        print("Hay encabezados vacíos.")
        valid_head = False

    #Algun header duplicado
    if len(set(normalized_headers)) != len(normalized_headers): #Validacion de encabezados (repetidos) set quita los repetidos
        print("Hay encabezados duplicados.")
        valid_head = False
    #Algun header faltante
    missing = [h for h in expected_headers if h not in normalized_headers] #Valida existencia de todos los headers esperados
    if missing: 
        print(f"Faltan encabezados requeridos: {missing}")
        valid_head = False
    return valid_head

def valid_row(row,headers, row_number): #Validacion de registros
    for h in headers:
        if row.get(h) is None:
            print(f"Fila {row_number} incompleta: falta {h}")
            row[h] = ""
        if None in row:
            print(f"Fila {row_number} tiene columnas extra: {row[None]}")
    return row
    
def csv_reader(p_path):
    list_of_games = []
    if not valid_size(p_path):
        return
    try:
        with open(p_path, "r", encoding="utf-8", newline="") as v_file:
            reader = csv.DictReader(v_file) #Con dict cambian las validaciones
            headers = reader.fieldnames
            if headers  is None:
                print("El archivo está vacío")
                return
            if not valid_headers(headers):
                return
            ##Fin de validaciones de encabezados
            
            row_number = 1 #Contador de filas, empieza en 1 para obviar el header
            has_data = False

            for item in reader:
                row_number += 1
                if not any(item.values()): # Se valida fila en blanco
                    continue
                has_data = True #se usará mas adelante para validar 2 El archivo viene vacio(caso 1 solo encabezados)
                item = valid_row(item, headers,row_number)
                list_of_games.append(item)
            if not has_data: # Se recorre todo el archivo y como no encontró lineas se muestra el error
                print("El archivo solo contiene encabezados, sin registros.")
            
            ##Fin de validaciones
            return list_of_games
            
    except FileNotFoundError: # 1 No hay archivo
        print(f"No se encontró el archivo: {p_path}")
    except UnicodeDecodeError:# 8 Codificación erronea (diferente a utf-8)
        print(f"No se pudo leer el archivo {p_path} con codificación UTF-8.")
    except Exception as e:# Algun caso no contemplado
        print(f"Ocurrió un error inesperado: {e}")

def genre_counter(p_list):
    temp_dict = {}
    for game in p_list:
        genre = game.get(HEAD_GENRE, "").capitalize()
        if genre in temp_dict:
            temp_dict[genre] += 1
        else:
            temp_dict[genre] = 1
    return temp_dict
        
games_list = csv_reader("csv_test.csv")
for key,value in genre_counter(games_list).items():
    print(f"{key}: {value}")