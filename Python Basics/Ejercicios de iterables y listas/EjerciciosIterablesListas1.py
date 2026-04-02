#Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
print("Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.")
first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "util"]
if len(first_list) == len(second_list):
    for i in range(len(first_list)):
        print(f"{first_list[i]} {second_list[i]}")
else:
    print("Las listas no son del mismo tamaño")

#Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
print("Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.")
my_string = "Cree un programa que itere e imprima un string letra por letra de derecha a izquierda"

for i in range(len(my_string)-1,-1,-1): #se hace con -1 para tomar en cuenta el 0 de posicionamiento de caracteres
    print(f"{my_string[i]}")

#Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.
print("Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.")
my_list1 = [4, 3, 6, 1, 7]
print(my_list1)
temp = my_list1[len(my_list1)-1]
my_list1[len(my_list1)-1] = my_list1[0]
my_list1[0] = temp
print(my_list1)

#Cree un programa que elimine todos los números impares de una lista.
print("Cree un programa que elimine todos los números impares de una lista.")
my_list2 = [1, 2, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9]
print(my_list2)
#Se intentó de esta manera pero el remove solo quita la primer ocurrencia del numero dando como resultado [2, 3, 3, 4, 6, 8]
#for number in my_list2:
#    if number % 2 != 0:
#        my_list2.remove(number)
#        print(f"Se removio el {number}")

#Se procede con pop en una lista inversa, debido a que remover o quitar elementos afectaría el tamaño y recorrimiento
for i in range(len(my_list2) - 1, -1, -1):
    if my_list2[i] % 2 != 0:
        my_list2.pop(i) 
print(my_list2)

#Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
print("Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.")
user_number = 0
number_list = []
highest = 0
for i in range(10):
    user_number = int(input(f"({i+1})Ingrese un numero "))
    number_list.append(user_number)
    if user_number>highest:
        highest=user_number
print(f"Numeros: {number_list} Mayor: {highest}" )

