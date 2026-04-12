"""
Cree una clase Rectangle que:
Tenga atributos width y height
Tenga un método get_area() que retorne el área
Tenga un método get_perimeter() que retorne el perímetro
Valide que ningún valor sea negativo. Si lo es, lance una excepción con un mensaje adecuado
"""
class Rectangle:
    def __init__(self, p_width, p_height):
        try:
            self.width = float(p_width)
            self.height = float(p_height)
            if self.p_width < 0 or self.p_height < 0 :
                raise ValueError("Existe un valor negativo, los valores deben ser positivos")
        except ValueError as e:
            print(f"Error: {e}")
    def get_area(self):
        return  self.width * self.height
    def get_perimeter(self):
        return (self.width * 2) + (self.height * 2)