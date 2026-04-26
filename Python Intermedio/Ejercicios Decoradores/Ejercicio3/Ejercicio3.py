"""
Cree una clase de User que:
Tenga un atributo de date_of_birth.
Tenga un property de age.
Luego cree un decorador para funciones que acepten un User como parámetro que se encargue de revisar si el User es mayor de edad y arroje una excepción de no ser así.
"""
from datetime import date
class User:
    def __init__(self, date_of_birth: date):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        birth = self.date_of_birth
        age = today.year - birth.year
        if today.month < birth.month:
            age -= 1
        elif today.month == birth.month:
            if today.day < birth.day:
                age -= 1
        return age
"""
--
Primer intento. 
Que pasa si es algo que no es USER pero que tambien tiene age?
Se descarta solución. 
Podría ser util para recorrer varios parametros USER con isinstance pero el ejercicio dice que las funciones acepten UN user. 
--
def valid_age(function):
    def wrapper(*args, **kwargs):
        for arg in args:
            try:
                if arg.age < 18:
                    raise ValueError("Menor de edad")
            except AttributeError: #Si no tiene el propertie entonces lo ignora.
                pass
        for kwarg in kwargs.values():
            try:
                if kwarg.age < 18:
                    raise ValueError("Menor de edad")
            except AttributeError:
                pass
        return function(*args,**kwargs)
    return wrapper
"""

def valid_age(function):
    def wrapper(user: User):
        if user.age < 18:
            raise ValueError("Menor de edad")
        return function(user)
    return wrapper

@valid_age
def print_user_age(user: User):
    print(f"El usuario tiene {user.age} años")

p_user = User(date(2005, 1, 1))#cambien la fecha para probar con un usuario mayor de edad.
try:
    print_user_age(p_user)
except ValueError as e:
    print(f"Error: {e}")