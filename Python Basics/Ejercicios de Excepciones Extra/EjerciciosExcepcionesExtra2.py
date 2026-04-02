def input_name(p_name):
    if p_name.isdigit():
        raise ValueError("El nombre no puede ser un numero")
    return p_name
def input_age(p_age):
    if not p_age.isdigit():
        raise ValueError("Numero no valido")
    return p_age
try:    
    name = input_name(input("Ingrese su nombre: "))
    age = input_age(input("Ingrese su edad: "))
    print(f"Hola {name}, su edad es {age}")
except ValueError as e:
    print(e)

def int_converter(p_list):
    number = 0
    for item in p_list:
        try:    
            number = int(item)
            print(f"'{item}' convertido a {number}")
        except ValueError as e:
            print(f"No se pudo convertir el elemento: {item}")
            continue       
my_list = ['4', 'hola', '10', '5.2']
int_converter(my_list)


def sum_values(p_list):
    total = 0
    for value in p_list:
        try:
            num = float(value)
            total += num
            print(f"{num} sumado correctamente")
        except (ValueError, TypeError):
            print(f"Elemento inválido: {value}")

    print(f"Total de la suma: {total}")
my_list = ['10', 'manzana', '5.5', '3', 'n/a', None]
sum_values(my_list)