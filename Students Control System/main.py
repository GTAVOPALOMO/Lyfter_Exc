from menu import start

def main():
    students = [] #Variable local que se envia por parametro.
    #Manejo de errores
    try:
    #Llamado del menú
        start(students)
    #Registros de errores
    except Exception as e:
        print(f"Error: {e}")

#Se define el entry point (sigue estando fuera de funciones pero asegura que no es una ejecución por imports)
if __name__ == "__main__":
    main()