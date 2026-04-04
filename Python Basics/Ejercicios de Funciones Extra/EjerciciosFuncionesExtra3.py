#Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto
def char_count(text, user_character):
    count = 0
    for character in text:
        if character.upper() == user_character.upper():
            count += 1
    return count
text = input("Ingrese la palabra: ")
character = input("Ingrese el caracter a buscar: ")
char_count(text, character)
print(f"Se ha encontrado {char_count(text, character)} veces el caracter {character}")


#Cree una función que reciba una lista de palabras y un número n, y retorne una nueva lista con solo las palabras que tengan más de n letras
def filter_words(word_list, number):
    temp_list = []
    for word in word_list:
        if len(word) > number:
            temp_list.append(word)
    return temp_list


input_list = ["cielo", "sol", "maravilloso", "día"]
min_char = int(input("Ingrese el numero de letras minimas en la palabra: "))
print(filter_words(input_list,min_char))

#Cree una función que reciba un string y retorne cuántas vocales contiene
def vowel_count(string):
    count = 0
    for character in string:
        if character.lower() in ("aeiouáéíóú"):
            count += 1
    return count

print(f"{vowel_count(input("Ingrese una palabra para contar sus vocales: "))}")
