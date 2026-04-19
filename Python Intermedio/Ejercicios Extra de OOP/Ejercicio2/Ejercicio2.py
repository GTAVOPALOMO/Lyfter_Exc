"""
Cree una clase base Animal y dos clases hijas Dog y Cat:
Animal debe tener nombre y método speak() que retorne "Hace un sonido"
Dog debe sobrescribir speak() para decir "Guau"
Cat debe sobrescribir speak() para decir "Miau"
"""
class Animal:
    def __init__(self, p_name):
        self.name = p_name
    def speak(self):
        return f"{self.name} hace un sonido"

class Dog(Animal):
    def speak(self):
        return f"{self.name} ladra"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} maulla"