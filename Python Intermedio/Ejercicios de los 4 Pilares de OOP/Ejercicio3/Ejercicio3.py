"""
Usos de herencia multiple
Según investigué, hay 2 conceptos clave en cuanto herencia multiple con Python.

MRO (Method Resolution Order):
    Es el orden en que Python busca métodos y atributos en una jerarquía de clases.
    En herencia múltiple, super() llama al siguiente método en ese orden.

Mixins -> Manera consistente, mantenible y escalable de aplicar herencia multiple en Python
    Un mixin es una clase pequeña que agrega una funcionalidad específica a otra clase.
    No está pensada para usarse sola, sino combinada con herencia múltiple.
    Se usa para reutilizar comportamiento sin crear jerarquías complejas.

Tomando en cuenta estos dos términos, podemos ver un ejemplo de dos maneras como lo hacemos acontinuación:    
"""
class Flyer:
    def move(self, action=None):
        return super().move(f"{action} volando")

class Swimmer:
    def move(self,action=None):
        return super().move(f"{action}, nadando")

class Walker:
    def move(self, action=None):
        return super().move(f"{action}, caminando")
#Esta clase se define para romper el recorrido de clases heredadas.
#Si no se agrega termina en Object y al intentar hacer Object.move cae.
class Base:
    def move(self, action=None):
        return action

class Duck(Flyer, Swimmer, Walker, Base):
    def move(self):
        return super().move("Soy un pato y estoy")
    pass

duck = Duck()
print(duck.move())  
"""
En este caso el pato al ejecutar la acción move gracias al MRO lo que hará es:
Primero su accion de move "Soy un pato y estoy"
Como esta accion está llamando a super() enviará esta accion al move del siguiente en la jerarquía el cual en este momento es Flyer
lo mismo con las siguientes clases hasta llegar a base.
La cual existe para evitar que hagan un super().move() a object el cual no tiene metodo move()
En que caso real podría ser útil?
Cuando se usan Mixins para darle diferentes cualidades a una clase.
Lo primero es corregir la mala práctica de hacer multi herencia con clases que comparten un mismo metodo.
"""
class FlyerMixin:
    def fly(self):
        return "volando"

class SwimmerMixin:
    def swim(self):
        return "nadando"
    
class WalkerMixin:
    def walk(self):
        return "caminando"
class Duck(FlyerMixin, SwimmerMixin, WalkerMixin):
    def exist(self):
        return f"Soy un pato y estoy {super().fly()}, {super().swim()}, {super().walk()}"
#NOTAS: Si hago override al metodo fly por ejemplo, deja de existir para el super()
#       Pasa al primer nivel de la jerarquia porque ahora debe llamarse con self

duck = Duck()
print(duck.exist())  

"""
En este caso el MRO busca los metodos correspondientes en la jerarquía de clases
Al no usar el mismo metodo evitamos ambiguedad
Un uso real podría ser hacer comportamientos independientes como Validar, Log, entre otros
Entonces al hacer clases ValidatorMixin, LoggerMixin podemos usar comportamientos genericos como validar y generar logs
los cuales tendremos centralizados en clases donde será facil dar mantenimiento, es mas escalable y consistente.
"""
