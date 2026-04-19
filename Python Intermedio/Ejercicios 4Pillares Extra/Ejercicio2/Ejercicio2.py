"""
Cree una clase abstracta User con los siguientes métodos abstractos:
get_role()
has_permission(permission)
Luego cree dos clases que hereden de ella:
AdminUser
RegularUser
Cada una debe implementar los métodos
Por ejemplo:
AdminUser siempre tiene permisos
RegularUser solo tiene permisos limitados ("read", por ejemplo)
"""
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, p_name):
        super().__init__()
        self.name = p_name
    @abstractmethod
    def get_role(self):
        pass
    @abstractmethod
    def has_permission(self,permission):
        pass
    
class AdminUser(User):
    def __init__(self, p_name):
        super().__init__(p_name)
    def get_role(self):
        return "Admin"
    def has_permission(self, permission):
        return True #Siempre tiene permisos como dice el enunciado
class RegularUser(User):
    def __init__(self, p_name):
        super().__init__(p_name)
        self.permissions = ["read"]
    def get_role(self):
        return "Regular"
    def has_permission(self, permission):
        return permission.strip().lower() in self.permissions