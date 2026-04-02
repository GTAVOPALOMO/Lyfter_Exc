
#Pasa los Ejercicios de Pseudocodigo previamente creados a código:
product_price = float(input("Ingrese el precio del producto "))
discounted_price = 0
if product_price < 100:
    discounted_price = product_price - (product_price * 0.02)
else:
    discounted_price = product_price - (product_price * 0.10)
print(discounted_price)
#########################################
time_in_seconds = int(input("Introduzca los segundos deseados "))
TIME_COMPARATOR = 600
if time_in_seconds > TIME_COMPARATOR:
    print("Mayor")
elif time_in_seconds < TIME_COMPARATOR:
    print(TIME_COMPARATOR - time_in_seconds)
else:
    print ("Igual")
#########################################
number = int(input("Ingrese un numero "))
temp = 0
for i in range(1,number+1): 
    temp += i
print(temp)
#########################################

#Pasa los Ejercicios de Diagramas de flujo previamente creados a código
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

#########################################

#numberList = []
num1 = 0
num2 = 0
num3 = 0
num1 = (int(input("Ingrese un numero ")))
num2 = (int(input("Ingrese un numero ")))
num3 = (int(input("Ingrese un numero ")))

if num1 == 30 or num2 == 30 or num3 == 30  or 30 == (num1+num2+num3):
    print("Correcto")
else:
    print("Incorrecto")

#Convertidor de unidades de temperatura
temp_celsius = float(input("Ingrese la temperatura en celsius "))
temp_fahrenheit = (temp_celsius * 9/5) + 32
temp_kelvin = temp_celsius + 273.15

print(f"Celsius: {temp_celsius} \n"
    f"Fahrenheit: {temp_fahrenheit} \n"
    f"Kelvin: {temp_kelvin} \n"
    )

#Tabla de multiplicar personalizada

table = int(input("Ingrese un numero del 1 al 10 "))
for i in range(12):
    print(f"{table} X {i+1} = {table * (i+1)}")
