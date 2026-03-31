from menu import start

def main():
    #Manejo de errores
    try:
    #Llamado del menú
        start()
    #Registros de errores
    except Exception as e:
        print(f"Error: {e}")

main()