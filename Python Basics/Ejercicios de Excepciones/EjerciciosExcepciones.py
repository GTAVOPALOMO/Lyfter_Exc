def menu():
    return "1.Suma\n2.Resta\n3.Multiplicación\n4.División\n5.Borrar resultado\n0.Salir\n"
def calc(number, actual_number, operation):
    match operation:
        case 1:
            return actual_number + number
        case 2:
            return actual_number - number 
        case 3:
            return actual_number * number
        case 4:
            try:
                return actual_number / number
            except ZeroDivisionError:
                print("No puede dividir entre 0")
                return actual_number
        case 5:
            return 0
        case _:
            return actual_number

def main():
    actual_number = 0
    while True:
        print(f"Actual number: {actual_number}")
        try:
            operation = int(input(f"{menu()}"))
            if operation > 5:
                raise ValueError
        except ValueError:
            print("Debe ingresar una opción válida del menú")
            continue
        if operation == 0:
            break
        if operation < 5:
            try:
                temp_number = float(input("Ingrese un numero para operar con el actual: "))
            except ValueError:
                print("Debe ingresar un numero válido")
                continue
        actual_number = calc(temp_number, actual_number,operation)

main()