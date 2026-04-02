
#Cree un programa que cuente cuántas veces aparece un número específico en una lista. Pida al usuario una lista de números y otro número a buscar
print("Cree un programa que cuente cuántas veces aparece un número específico en una lista. Pida al usuario una lista de números y otro número a buscar")
num_list = []
stopper = False
user_number = 0
count = 0
while not stopper:
    num_list.append(int(input("Ingrese un numero: ")))
    choice = input("Desea ingresar otro numero? Y/N ")
    if choice.upper() == 'N':
        stopper = True
print(num_list)
user_number = int(input("Ingrese el numero que desea contar en la lista: "))

for number in num_list:
    if user_number == number:
        count += 1

print(f"Hay {count} iteraciones del numero {user_number}")

#Cree un programa que verifique si todos los elementos de una lista son positivos
print("Cree un programa que verifique si todos los elementos de una lista son positivos")
my_list = [3, 6, 0, -2, 4]
non_positive = False
for number in my_list:
    if number <= 0 :
        non_positive = True
        print("Hay al menos un numero negativo o cero")
        break
if not non_positive:
    print("Solo hay positivos")

#Cree un programa que muestre el valor más pequeño de una lista sin usar min().
print("Cree un programa que muestre el valor más pequeño de una lista sin usar min().")
my_list2 = [9, 4, 7, 5, 1]
min_num = my_list2[0]
#No se usa esta solución porque tiene una iteración redundante cuando compara el primer numero (siempre van a ser iguales)
#for number in my_list2 :
#    if min_num > number :
#        min_num = number
#En esta solucion usamos el i+1 como pivote del index para recorrer la lista completa sin generar array out of bounds con un len - 1. Se recorren justamente los elementos que se deben recorrer
for i in range(len(my_list2)-1):
    if min_num > my_list2[i+1] :
        min_num = my_list2[i+1]
print(f"El numero menor es: {min_num}")

#Cree un programa que reciba una lista de números y calcule el promedio de los valores, luego cree una nueva lista con solo los valores mayores al promedio
my_list = [10, 20, 30, 40, 50]
total = 0
count = len(my_list)
prom = 0
new_list = []
for item in my_list:
    total += item
prom = total/count
for item in my_list:
    if item > prom:
        new_list.append(item)
print(f"El promedio es: {prom} y la nueva lista es: {new_list}" )


#Cree un programa que le pida al usuario ingresar 5 palabras. Luego muestre una nueva lista con solo aquellas palabras que tengan más de 4 letras
print("Cree un programa que le pida al usuario ingresar 5 palabras. Luego muestre una nueva lista con solo aquellas palabras que tengan más de 4 letras")
word_list = []
for i in range(5):
    temp_word = input("Ingrese una palabra ")
    if len(temp_word) > 4:
        word_list.append(temp_word)
print(word_list)