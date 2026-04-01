import csv
import os
#Se intenta resolver el ejercicio considerando edge cases posibles
#Posibles edge cases en lecturas de archivos:
# 1 No hay archivo
# 2 El archivo viene vacio(caso 1 solo encabezados, caso 2 ni siquiera encabezados)
# 3 El archivo es demasiado grande
# 4 Los registros vienen mal(caso 1 menos columnas que encabezados, caso 2, mas columnas que encabezados)
# 5 Hay filas en blanco
# 6 No se respeta el formato de archivo esperado (minimo tiene los encabezados requeridos)
# 7 Se duplicaron encabezados
# 8 Codificación erronea (diferente a utf-8)
# 9 separador diferente a la coma-------No se como validarlo en python
#       tal vez con el caso de validacion de headers sea suficiente para capturarlo. 
#
## Favor indicar si existen edge cases que no se estén contemplando.
def csv_reader(p_path):
    MAXIMUM_SIZE = 500
    HEADERS = ["Name","Genre","Developer","ESRB"]
    try:
        file_size = os.path.getsize(p_path)
        if file_size>= MAXIMUM_SIZE: # 3 El archivo es demasiado grande
            print(f"El tamaño del archivo[{file_size}] es superior al máximo permitido[{MAXIMUM_SIZE}]")
            return

        with open(p_path, "r", encoding="utf-8", newline="") as v_file:
            reader = csv.reader(v_file)
            try:
                headers = next(reader) #2 El archivo viene vacio(caso 2)
            except StopIteration:
                print("El archivo está vacío.")
                return    
            normalized_headers = [h.strip().lower() for h in headers]
            expected_headers = [h.strip().lower() for h in HEADERS]
            if any(h == "" for h in normalized_headers): #Validacion de encabezados (Vacios)
                print("Hay encabezados vacíos.")
                return
            if len(set(normalized_headers)) != len(normalized_headers): #Validacion de encabezados (repetidos) set quita los repetidos
                print("Hay encabezados duplicados.")
                return
            missing = [h for h in expected_headers if h not in normalized_headers] #Valida existencia de todos los headers esperados
            if missing: 
                print(f"Faltan encabezados requeridos: {missing}")
                return
            

            if not headers: # 5 Hay filas en blanco (en este caso encabezado)
                print("El archivo no contiene encabezados válidos.")
                return
            ##Fin de validaciones de encabezados
            row_number = 1 #Contador de filas
            has_data = False
            for item in reader:
                row_number += 1
                if not item: # 5 Hay filas en blanco
                    continue
                has_data = True #se usará mas adelante para validar 2 El archivo viene vacio(caso 1 solo encabezados)
                if len(item) < len(headers): # 4 Los registros vienen mal
                    print(f"Fila {row_number} incompleta: {item}")
                    item += [""] * (len(headers) - len(item)) #(si vienen menos que encabezados se completan los espacios vacios)

                elif len(item) > len(headers):# 4 Los registros vienen mal
                    print(f"Fila {row_number} tiene columnas extra: {item}")
                    item = item[:len(headers)] # (si vienen más que encabezados se ignoran)
                #Se recorre la lista de headers y la del item correspondiente al row
                for i in range(len(headers)):
                    print(f"{headers[i].strip()}: {item[i].strip()}")
                print()

            if not has_data: # Se recorre todo el archivo y como no encontró lineas se muestra el error
                print("El archivo solo contiene encabezados, sin registros.")

    except FileNotFoundError: # 1 No hay archivo
        print(f"No se encontró el archivo: {p_path}")
    except UnicodeDecodeError:# 8 Codificación erronea (diferente a utf-8)
        print(f"No se pudo leer el archivo {p_path} con codificación UTF-8.")
    except Exception as e:# Algun caso no contemplado
        print(f"Ocurrió un error inesperado: {e}")

csv_reader("csv_test.csv")

