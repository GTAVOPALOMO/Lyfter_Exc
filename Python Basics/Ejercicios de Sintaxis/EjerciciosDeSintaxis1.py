########################################################################################################################################################################################################
# 1 Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.
variable_string = "Text"
variable_int = 10
variable_list = [1,"2",'3',4.0]
variable_float = 2.5
variable_bool = False

#Validacion de tipos
#print(
#f"variable_string: {type(variable_string)}\n"
#f"variable_int: {type(variable_int)}\n"
#f"variable_list: {type(variable_list)}\n"
#f"variable_float: {type(variable_float)}\n"
#f"variable_bool: {type(variable_bool)}   " 
#)

#string + string → ?
#print(variable_string + variable_string)
#RESULTADO: Logra concatenar los dos strings
#string + int → ?
#print(variable_string + variable_int)
#RESULTADO: TypeError: can only concatenate str (not "int") to str (Solo puede concatenar otro string a string)
#int + string → ?
#print(variable_int + variable_string)
#RESULTADO: TypeError: unsupported operand type(s) for +: 'int' and 'str' no ecuentra operador valido entre enteros y strings, y no existe alguno por ahora. 
#list + list → ?
#print(variable_list + variable_list)
#RESULTADO: Concatena las listas con éxito
#string + list → ?
#print(variable_string + variable_list)
#RESULTADO: El mismo que concatenar cualquier cosa a un string que no sea un string.
#float + int → ?
#print(variable_float + variable_int)
#RESULTADO: Suma ambos valores al ser numéricos
#bool + bool → ?
#print(variable_bool + variable_bool)
#RESULTADO: Se imprime un 2 cuando los dos valores son True. 
#bool + string
#print(variable_bool + variable_string)
#RESULTADO: El bool se comporta similar a un numérico, requiere un operador válido
#bool + int
#print(variable_bool + variable_int)
#RESULTADO: Se comprueba que el valor true del bool equivale a un numerico de valor 1 y el false 0


#CONCLUSION: Después de investigar se hace la comprobación que por diseño del lenguaje python, el bool es una clase que hereda de int. Esto tiene muchas implicaciones a nivel de uso.
########################################################################################################################################################################################################

########################################################################################################################################################################################################
# 2 Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.

var_name = input("Ingrese su nombre y apellido: ")
var_age = int(input("Ingrese su edad: "))
var_phase = ""
var_message = f"Estimad@ {var_name} usted es "

if 0 <= var_age <= 2:
    var_phase = "bebé"
elif 2 < var_age <= 9:
    var_phase = "niño"
elif 9 < var_age <= 12:
    var_phase = "preadolescente"
elif 12 < var_age <= 17:
    var_phase = "adolescente"
elif 17 < var_age <= 29:
    var_phase = "adulto Joven"
elif 29 < var_age <= 64:
    var_phase = "adulto"
elif 64 < var_age:
    var_phase = "adulto Mayor"
else:
    var_phase = "una anomalía"
print(var_message + var_phase)
########################################################################################################################################################################################################

########################################################################################################################################################################################################
# 3 Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.
import random
is_guessed = False
var_random = random.randint(1,10)
user_number = 0

while not is_guessed :
    user_number = int(input("Ingresa un numero del 1 al 10: "))
    if var_random == user_number:
        print("FELICIDADES! GANASTE!")
        is_guessed = True
    else:
        print("Vuelvelo a intentar!")

########################################################################################################################################################################################################

########################################################################################################################################################################################################
#4Cree un programa que le pida tres números al usuario y muestre el mayor.
list_var = []
while len(list_var) < 3:
    list_var.append(int(input(f"Ingrese un numero, {len(list_var)+1} de 3: ")))
print(max(list_var))
########################################################################################################################################################################################################

########################################################################################################################################################################################################
#5 Dada n cantidad de notas de un estudiante, calcular:
#Cuantas notas tiene aprobadas (mayor a 70).
#Cuantas notas tiene desaprobadas (menor a 70).
#El promedio de todas.
#El promedio de las aprobadas.
#El promedio de las desaprobadas.
########################################################################################################################################################################################################

students_grades = []
stopper = False
choice = ""
approved_count = 0
rejected_count = 0
all_average = 0
approved_total = 0
rejected_total = 0

while not stopper:
    students_grades.append(int(input(f"Notas ingresadas: {len(students_grades)} Ingrese una nota: ")))
    choice = input("Desea ingresar otra? Y/N ")
    if choice.upper() not in ("Y","N"):
        choice = input("Ingrese una opción válida: ")
    if choice.upper() == "N":
        stopper = True

for grade in students_grades:
#Cuantas notas tiene aprobadas (mayor a 70).
    if grade >= 70:
        approved_count += 1
        approved_total += grade
#Cuantas notas tiene desaprobadas (menor a 70).
    else:
        rejected_count += 1
        rejected_total += grade

#El promedio de todas.
print(f"Promedio de todas: {sum(students_grades)/len(students_grades)}")
#El promedio de las aprobadas.
print(f"Promedio de aprobadas: {approved_total/(approved_count or 1)}")
#El promedio de las desaprobadas.
print(f"Promedio de reprobadas: {rejected_total/(rejected_count or 1)}")

