"""
Cree un decorador que haga print de los parámetros y retorno de la función que decore.
"""
def decorator_example(function):
    def wrapper(*args, **kwargs):
        print(f"Parámetros: {args}, {kwargs}")
        result = function(*args, **kwargs)
        print(f"Retorno: {result}")
        return result
    return wrapper

@decorator_example
def test_function(X :int, number :int = 20):
    return X + number


test_function(int(input("Ingrese un número: ")), number=int(input("Ingrese otro número: ")))