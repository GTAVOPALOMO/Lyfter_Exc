"""
Cree una función que imprima “Hola, [nombre]” dos veces:
Cree un decorador @repeat_twice que haga que la función decorada se ejecute dos veces seguidas, con los mismos argumentos
"""
def repeat_twice(f):
    def wrapper(*args,**kwargs):
        f(*args,**kwargs)
        f(*args,**kwargs)
    return wrapper


@repeat_twice
def print_hi(name):
    print(f"Hola {name}")

print_hi("Gustavo")