var_global = 320
#Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.
def printMessageSecond():
    var_message = "Segundo mensaje"
    print(var_message)

def printMessageFirst():
    print("Primer mensaje")
    printMessageSecond()

printMessageFirst()


#Experimente con el concepto de scope
##Intente acceder a una variable definida dentro de una función desde afuera.
#print(var_message) No logra verla porque esta fuera de scope en la función printMessageSecond
##Intente acceder a una variable global desde una función y cambiar su valor.
print(var_global)
def change_value():
    var_global = 100
    print(var_global)
change_value()
print(var_global)
#No hubo cambio de valor a nivel global
def change_value_global():
    global var_global 
    var_global = 100
    print(var_global)
change_value_global()
print(var_global)
#Ahora si cambia porque en la funcion se referencia con global


#Cree una función que retorne la suma de todos los números de una lista.
def list_sum(p_list):
    total = 0
    for number in p_list:
        total += number
    return total

print(list_sum([4, 6, 2, 29]))

#Cree una función que le dé la vuelta a un string y lo retorne
def backwards_word(word):
    new_word = ""
    for i in range(len(word)-1,-1,-1): 
        new_word += word[i]
    return new_word

print(backwards_word("backwards String"))

#Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string
def upper_lower_count(p_word):
    upper_count = 0
    lower_count = 0
    for char in p_word:
        if char.isupper():
            upper_count += 1
        else:
            lower_count += 1
    return f"Mayusculas: {upper_count} Minusculas: {lower_count}"

print(upper_lower_count("AaBbCcABCDunodostreS"))

#Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.
def order_words(words):
    word_list = words.split('-')
    word_list.sort()
    return '-'.join(word_list)

print(order_words("python-variable-funcion-computadora-monitor"))

#Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.

def is_prime(number):
    #caso 1 es menor o igual a 1
    if number <= 1:
        return False
    #caso 2 si es par y mayor que 2
    if number % 2 == 0 and number > 2:
        return False
    #caso reducido, los numeros impares que vayan desde 2 hasta la raiz cuadrada del numero
    #Si un numero tiene divisor debe estar antes de su raíz cuadrada que es lo mismo que la potencia a un medio o 0.5
    for i in range(3, int(number**0.5) + 1,2): # se avanza en el rango de 2 en 2 para ver solo impares
        if number % i == 0 :
            return False
    return True

def obtain_prime(number_list):
    primes = []
    for number in number_list:
        if is_prime(number):
            primes.append(number)
    return primes

print(obtain_prime([1, 4, 6, 7, 13, 9, 67] ))

