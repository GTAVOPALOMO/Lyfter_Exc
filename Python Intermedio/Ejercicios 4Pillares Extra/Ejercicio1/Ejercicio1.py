"""
Cree una clase Employee con los siguientes requisitos:
Atributos privados: _name, _salary
Use @property y @<atributo>.setter para:
Mostrar el nombre y el salario
Validar que el salario nunca sea negativo
Cree un método promote que aumente el salario un porcentaje definido
"""
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary  # usamos el setter para validar desde el inicio
#name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value
#salary
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("El salario no puede ser negativo")
        self.__salary = value
#Methods
    def promote(self, percentage):
        self.__salary += self.__salary * percentage
