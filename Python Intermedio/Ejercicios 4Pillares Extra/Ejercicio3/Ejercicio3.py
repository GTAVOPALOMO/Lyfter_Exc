"""
Cree una clase base Vehicle con los atributos:
_brand
_year
Agregue un método get_info() que devuelva una descripción del vehículo.
Luego cree dos clases hijas:
Car
Motorcycle
Cada una debe agregar su propio atributo (por ejemplo, doors o type) y sobrescribir el método get_info() para incluir esta información adicional.
"""
class Vehicle:
    def __init__(self, p_brand, p_year):
        self.__brand = p_brand
        self.__year = p_year
    
    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self, value):
        self.__brand = value

    @property
    def year(self):
        return self.__year
    @brand.setter
    def year(self, value):
        self.__year = value

    def get_info(self):
        return f"{self.brand} ({self.year})"

class Car(Vehicle):
    def __init__(self, p_brand, p_year, p_doors):
        super().__init__(p_brand, p_year)
        self.__doors = p_doors
    
    @property
    def doors(self):
        return self.__doors
    @doors.setter
    def year(self, value):
        self.__doors = value

    def get_info(self):
        return super().get_info() + f" - Puertas: {self.doors}"
    

class Motorcycle(Vehicle):
    def __init__(self, p_brand, p_year, p_type):
        super().__init__(p_brand, p_year)
        self.__type = p_type
    
    @property
    def type(self):
        return self.__type
    @type.setter
    def year(self, value):
        self.__type = value

    def get_info(self):
        return super().get_info() + f" - Tipo: {self.type}"
