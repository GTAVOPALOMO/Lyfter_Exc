import json
import logging

FILE_LOGGER = "FILE_LOG"
ERROR_LOGGER = "ERR_LOG"
SUPPORTED_LANGUAGES = ["japanese", "english", "french", "german", "korean", "chinese"]
SUPPORTED_ATTRIBUTES = ["name", "level", "type", "base"]
SUPPORTED_STATS = ["HP","Attack","Defense","Sp. Attack","Sp. Defense","Speed"]
ORIGIN_FILE = "FILE"
ORIGIN_MEMORY = "MEMO"
#Permite crear una clase que configure los logs
def setup_logging(p_exercise_name):
    #Como buena práctica se debe definir una ruta, para estos casos de ejercicios no lo haremos
    #os.makedirs.....
    log_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    #logs de archivos
    file_log = logging.getLogger(FILE_LOGGER)
    file_log.setLevel(logging.ERROR)
    file_log.propagate = False # Esto es para que no escriban en el log raíz o duplicar los registros en otros archivos
    #handler de files
    file_log_handler = logging.FileHandler("file_"+p_exercise_name+".log", encoding="utf-8")
    file_log_handler.setFormatter(log_format)
    file_log_handler.setLevel(logging.ERROR)
    
    #log de otros errores
    error_log = logging.getLogger(ERROR_LOGGER)
    error_log.setLevel(logging.ERROR)
    error_log.propagate = False # Esto es para que no escriban en el log raíz o duplicar los registros en otros archivos
    #handler de errores
    error_log_handler = logging.FileHandler("error_"+p_exercise_name+".log", encoding="utf-8")
    error_log_handler.setFormatter(log_format)
    error_log_handler.setLevel(logging.ERROR)

    #Se deben crear los handlers para llamarlos en otros metodos.
    #El handler debe ser del error y no del handler
    if not error_log.handlers:
        error_log.addHandler(error_log_handler)
    if not  file_log.handlers:   
        file_log.addHandler(file_log_handler)

def json_read(p_path):
    #inicialización del logger
    read_logger = logging.getLogger(FILE_LOGGER)
    poke_list = []
    try:
        with open(p_path, encoding="utf-8") as v_file:
            reader = json.load(v_file)
            for item in reader:
                poke_list.append(item)
    except Exception as e:
        #traceback.print_exc() #Nos puede servir para guardar en logs técnicos.
        #Investigando encontré traceback, pero investigando más veo que python tiene logging para manejar lo mismo.
        read_logger.exception(e)
    return poke_list

def json_write(p_path, data):
    with open(p_path, "w", encoding="utf-8") as v_file:
        json.dump(data, v_file, indent=4)#ident 4 para que sea legible


def language_selection():
    for key,value in (enumerate(SUPPORTED_LANGUAGES)):
        print(f"[{key}] - {value.capitalize()}")
    return int(input("Seleccione un idioma: "))

def choice_selector(text):
    options = {"Y" : True, "N" : False}
    return bool(options.get(input(text).upper(),False))#Cualquier otra cosa que no sea y o Y será FALSE

def validate_structure(data, position, origin):
    #Se define a cual logger va a escribir dependiendo del origen del llamado del metodo
    if origin == ORIGIN_FILE:
        logger = FILE_LOGGER
    else:
        logger = ERROR_LOGGER
    error_logging = logging.getLogger(logger)
    #La estructura esperada es:
    #   "name"      :   {str : str}
    #   "level"     :   int
    #   "type"      :   [str,...,str]
    #   "base"      :   {"HP": int,
    #                    "Attack": int,
    #                    "Defense": int,
    #                    "Sp. Attack": int,
    #                    "Sp. Defense": int,
    #                    "Speed": int}
    # Por lo cual se debe validar que el archivo respete esa estructura antes y despues de la escritura#
    
    #Valida formato JSON valido
    if not isinstance(data,dict):
        error_logging.error(f"Error con el diccionario: {item} en la posición {position}")
        return False
    #valida que tenga todos los atributos
    for item in SUPPORTED_ATTRIBUTES:
        if item not in data:
            error_logging.error(f"Error, falta {item} en la posición {position} \nPOKEMON: \n{data}")
            return False
        #valida estrucutra del name un diccionario de str : str
        if item == SUPPORTED_ATTRIBUTES[0]:
            #primero valida que sea un dict
            # luego recorre el diccionario y valida que cada key y value sean str       
            if not (isinstance(data[item], dict) and all(isinstance(language,str) and isinstance(poke_name,str) for language,poke_name in data[item].items())): 
                error_logging.error(f"Error con la estructura del nombre : {item} en la posición {position}")
                return False
        #valida estructura del level un int
        if item == SUPPORTED_ATTRIBUTES[1]:
            if not isinstance(data[item], int):
                error_logging.error(f"Error con la estructura del nivel : {item} en la posición {position}")
                return False
        #valida estructura del type (una lista de strings)
        if item == SUPPORTED_ATTRIBUTES[2]:
            if not (isinstance(data[item], list) 
                    and all(isinstance(poke_type, str) for poke_type in data[item])):
                error_logging.error(f"Error con la estructura del tipo : {item} en la posición {position}")
                return False
        #valida estructura del base
        if item == SUPPORTED_ATTRIBUTES[3]:
            #primero valida que sea un dict correcto
            #luego valida que todos los stats esten en el dict y su valor sea entero
            print(f"Lista de stats: ")
            print(data[item].items())
            if not (isinstance(data[item], dict) 
                    and all(stat in SUPPORTED_STATS and isinstance(val,int) for stat,val in data[item].items()) 
                    and all(valid_stat in data[item].keys() for valid_stat in SUPPORTED_STATS)):
                error_logging.error(f"Error con la estructura de los stats (base) : {data[item]} en la posición {position}")
                return False   
    return True

def main():
    try:
        #Se inicia el logger de la aplicación
        setup_logging("EjerciciosJSON") 
        error_logging = logging.getLogger(ERROR_LOGGER)
        path = input("Ingrese el nombre del archivo: ")
        #lectura del archivo y almacenamiento en lista
        poke_list = json_read(path)
        #Si no se encuentra el archivo
        if not poke_list:
            raise Exception("No hay lista, vuelva a intentarlo")
        #validar formato del archivo
        for i, pokemon in enumerate(poke_list):
            if not validate_structure(pokemon, i, ORIGIN_FILE):
                raise Exception("Error de formato con un pokemon, vuelva a intentarlo")
        #teniendo el archivo en memoria como un dict podemos modificarlo a gusto
        language = -1
        selection = True
        while selection:
                temp_pokemon = {}
                #captura del nombre del pokemon en idiomas disponibles
                print("INGRESO DEL NOMBRE: ")
                temp_name = {}
                selection = True
                while selection:
                    language = language_selection()
                    poke_name = input(f"Ingrese el nombre del pokemon en el idioma escogido [{SUPPORTED_LANGUAGES[language].capitalize()}]: ")
                    #Valida nombres vacios
                    if not poke_name:
                        raise Exception("Debe ingresar un nombre válido")
                    temp_name[SUPPORTED_LANGUAGES[language]] = poke_name
                    selection = choice_selector(f"Desea agregar un nombre en otro idioma o corregir el agregado en {SUPPORTED_LANGUAGES[language].capitalize()} [Y/N]: ")
                temp_pokemon["name"] = temp_name
                #captura del nivel del pokemon
                print("INGRESO DEL NIVEL: ")
                poke_level = int(input("Ingrese el nivel: "))
                if poke_level <= 0:
                    raise Exception("Debe ingresar un valor mayor a 0")
                temp_pokemon["level"] = poke_level
                
                #Captura de tipos
                print("INGRESO DE TIPOS: ")
                poke_types = []
                selection = True
                while selection:
                    temp_type = input("Ingrese un tipo: ")
                    poke_types.append(temp_type)
                    selection = choice_selector(f"Tipos actuales: {poke_types} \nDesea agregar otro tipo? [Y/N]: ")
                temp_pokemon["type"] = poke_types

                #captura de base (stats)
                temp_hp = int(input("Ingrese el HP: "))
                temp_atk = int(input("Ingrese el ataque: "))
                temp_def = int(input("Ingrese la defensa: "))
                temp_spatk = int(input("Ingrese la el atk especial: "))
                temp_spdef = int(input("Ingrese la la def especial: "))
                temp_speed = int(input("Ingrese la velocidad: "))
                temp_stats =  { "HP": temp_hp,
                                "Attack": temp_atk,
                                "Defense": temp_def,
                                "Sp. Attack": temp_spatk,
                                "Sp. Defense": temp_spdef,
                                "Speed": temp_speed}
                if not all(value >= 0 for value in temp_stats.values()):
                    raise Exception("Debe ingresar un valor mayor a 0")
                temp_pokemon["base"] = temp_stats
                print(temp_pokemon)
                #se valida la estructura del dict
                if not validate_structure(temp_pokemon,0,ORIGIN_MEMORY):
                    print("Error de formato con el pokemon ingresado, vuelvalo a intentar")
                    continue
                
                #Se agrega el pokemon a la lista
                poke_list.append(temp_pokemon)
                selection = choice_selector("Desea agregar otro pokemon? [Y/N]: ")
                
                if not selection:
                    #Se graba en el archivo
                    json_write(path, poke_list)
                    return selection
    except Exception as e:
        print("*******************ERROR*******************")
        print(e)
        error_logging.exception(e)
        return True

if __name__ == "__main__":
    choice = True
    while choice:
        choice = main()
