"""
Cree una función que se llame multiply, la cual obtiene dos valores y los multiplica entre si
A esta función se le debe combinar dos decoradores:
@log_call: imprime el nombre de la función, los argumentos, fecha actual y el retorno
@validate_numbers: revisa que todos los argumentos sean numéricos
"""
from datetime import datetime
def log_call(f: function):
    def w(a,b):
        print(f"Funcion: {f.__name__}")
        print(f"Parametros: {a}, {b}")
        print(datetime.today())
        result = f(a,b)
        print(result)
        return result
    return w

def validate_numbers(f: function):
    def wrap(*args,**kwargs):
        for a in args:
            if not isinstance(a,int):
                raise ValueError(f"{a} no es numerico")
        for k in kwargs.values():
            if not isinstance(k,int):
                raise ValueError(f"{a} no es numerico")
        return f(*args,**kwargs)
    return wrap

#El orden importa para tomar el nombre de la función. Es jerarquico
@validate_numbers
@log_call
def multiply(val1, val2):
    return val1*val2


try:
    print(multiply(3,2))
except Exception as e:
    print(f"Error: {e}")