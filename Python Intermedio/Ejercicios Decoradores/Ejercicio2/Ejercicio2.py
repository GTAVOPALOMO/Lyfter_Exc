"""
Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.
"""
def has_ints(function):
    def wrapper(*args,**kwargs):
        for arg in args:
            if not isinstance(arg,int):
                raise ValueError(f"{arg} no esta siendo interpretado como numero")
        for kwarg in kwargs.values():
            if not isinstance(kwarg,int):
                raise ValueError(f"{kwarg} no esta siendo interpretado como numero")
        return function(*args, **kwargs)
    return wrapper

@has_ints
def printer(p_number1, p_number2):
    print(f"Ingresó {p_number1} y {p_number2}")


try:
    printer(3,p_number2=2)
except ValueError as e:
    print(f"Error: {e}")