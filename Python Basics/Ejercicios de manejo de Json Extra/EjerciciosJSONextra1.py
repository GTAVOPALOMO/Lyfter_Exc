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
            if not (isinstance(data[item], dict) 
                    and all(stat in SUPPORTED_STATS and isinstance(val,int) for stat,val in data[item].items()) 
                    and all(valid_stat in data[item].keys() for valid_stat in SUPPORTED_STATS)):
                error_logging.error(f"Error con la estructura de los stats (base) : {data[item]} en la posición {position}")
                return False   
    return True

def print_poke(poke_list,detailed):
        for poke in poke_list:
            print(f"Nombre del pokemon: {poke["name"]}")
            if detailed:
                print(f"Nivel del pokemon: {poke["level"]}")
                print(f"Tipos:")
                for _type in poke["type"]:
                    print(f"\t{_type}")
            print(f"Stats:")
            for stat, value in poke["base"].items():
                print(f"\t{stat} : {value}")
def search_type(poke_list,user_type): #Se intenta utilizar list comprehension
    #Retorna lista conformada por
    return [
        #un pokemon
        pokemon
        #por cada pokemon en la lista
        for pokemon in poke_list
        #si el tipo ingresado esta en la lista de tipos del pokemon
        if user_type.lower() in [poke_type.lower() for poke_type in pokemon["type"]] 
    ]

def type_average_level(poke_list):
    #Solución optima *********Es optima porque no estoy guardando arreglos de los niveles, estoy guardando sumas y conteos que eventualmente los iba a calcular. Mejor almaceno el calculo directamente
    #La solución óptima para escalabilidad es el for pero sin usar listas temporales
    #en el mismo diccionario almacenamos el conteo del nivel y la suma para no tener que recorrer N listas sumando y calculando tamaño para obtener el average
    temp_dict = {}
    for pokemon in poke_list:
        for _type in pokemon["type"]:
            if _type not in temp_dict:
                temp_dict[_type] = {"sum": pokemon["level"], "count": 1}
            else:
                temp_dict[_type]["sum"] += pokemon["level"]
                temp_dict[_type]["count"] += 1
    
    for key, value in temp_dict.items():
        print(f"Tipo: {key}, Nivel promedio: {value["sum"]/value["count"]}")
    
    #implementacion del dictionary comprehension para return
    return {key: value["sum"]/value["count"] for key, value in temp_dict.items() }


    #Solucion usando comprehension de estructuras ***********RENDIMIENTO Y ESCALABILIDAD MENOR por como la usaba.
    ##DICTCIONARY COMPREHENSION
    ##temp_dict = {
    #    #implementando Generator Expression con built-in functions
    #    #se logra obtener de cada pokemon en la lista la suma de los niveles
    #    #siempre y cuando el type obtenido del set se encuentre en los tipos del pokemon
    #    _type: sum(pokemon["level"] for pokemon in poke_list if _type in pokemon["type"])
    #            /len([pokemon for pokemon in poke_list if _type in pokemon["type"]])
    #    #por cada tipo en el set
    #    for _type in 
    #    #SET COMPREHENSION
    #    #Me permitirá tomar todos los tipos sin repetir 
    #    {inner_type for inner_pokemon in poke_list for inner_type in inner_pokemon["type"]}
        
        
    #}
    #for key, value in temp_dict.items():
    #        print(f"Tipo: {key}, Nivel promedio: {value}")

    #temp_dict = {}
    ##para promediar el nivel por tipo primero debemos almacenar todos los niveles que existen de cada pokemon por cada tipo
    ##ejemplo: fuego : [20,18...,int]
    #for item in poke_list:
    #    for _type in item["type"]:
    #        if _type not in temp_dict.keys():
    #            temp_dict[_type] = [item["level"]]
    #        else:
    #            temp_dict[_type].append(item["level"])
    ##despues con un dict formato typo : [nivel, ..., nivel] es posible calcular el promedio facilmente con suma total entre len
    #for key, lvl_list in temp_dict.items():
    #    temp_dict[key] = sum(lvl_list) / len(lvl_list)
    #    print(f"Tipo: {key}, Nivel promedio: {temp_dict[key]}")
    #return temp_dict

def main():
    try:
        #Se inicia el logger de la aplicación
        setup_logging("EjerciciosJSONextra1") 
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
        
        #Logica de ejercicios:
        
        #Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
        #Recorra la lista de Pokémon y muestre en consola su nombre, tipo y nivel (o cualquier otro atributo definido)
        print_poke(poke_list, True)
        
        #Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
        #Pida al usuario un tipo de Pokémon
        #Muestre todos los Pokémon que sean de ese tipo
        user_type = input("Ingrese un tipo: ")
        print_poke(search_type(poke_list,user_type), True) #hacemos una funcion que devuelva la lista para asi imprimir los encontrados
    
        #Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
        #Para cada Pokémon, muestre sus estadísticas principales (por ejemplo: ataque, defensa, velocidad, etc.)
        #en la función print ya se consideran los stats. se agrega un boolean para imprimir detallado o no la info
        print_poke(poke_list, False)

        #Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
        #Agrupe los Pokémon por tipo (por ejemplo, "agua", "fuego", etc.)
        #Calcule y muestre el promedio de nivel para cada tipo:
        type_average_level(poke_list)

    except Exception as e:
        print("*******************ERROR*******************")
        print(e)
        error_logging.exception(e)

if __name__ == "__main__":
    main()
