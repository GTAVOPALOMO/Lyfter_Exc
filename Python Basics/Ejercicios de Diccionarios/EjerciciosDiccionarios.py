# Cree un diccionario que guarde la siguiente información sobre un hotel:
print("Cree un diccionario que guarde la siguiente información sobre un hotel:")
dic = {
    "name": "Hotel",
    "stars": 5,
    "rooms": [
        {"Number": 1, "Floor": 2, "price_per_night": 39.99},
        {"Number": 2, "Floor": 2, "price_per_night": 39.99},
        {"Number": 3, "Floor": 3, "price_per_night": 99.99},
    ],
}
print(dic)

#Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
print("Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.")
list_a = ["first_name", "last_name", "role"]
list_b = ["Gustavo", "Palomo", "Unemployed"]
dictionary = {}

#Solución A usando dict y zip
dictionary = dict(zip(list_a,list_b))
#Solución B ciclando
for i in range(len(list_a)):
    dictionary[list_a[i]] = list_b[i]
print(dictionary)
#La solución A nunca va a reventar por un index out of bounds, pero omitirá elementos si las listas son de diferente tamaño

#Cree un programa que use una lista para eliminar keys de un diccionario.
print("Cree un programa que use una lista para eliminar keys de un diccionario.")
list_of_keys = ["access_level", "age"]
employee = {"name": "John", "email": "john@ecorp.com", "access_level": 5, "age": 28}
print(employee)
for key in list_of_keys:
    employee.pop(key)
print(employee)
