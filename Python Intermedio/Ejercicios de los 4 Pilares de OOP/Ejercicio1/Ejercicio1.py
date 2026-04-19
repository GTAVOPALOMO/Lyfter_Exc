"""
Cree una clase de BankAccount que:
Tenga un atributo de balance.
Tenga un método para ingresar dinero.
Tengo un método para retirar dinero.
Cree otra clase que herede de esta llamada SavingsAccount que:
Tenga un atributo de min_balance que se pueda asignar al crearla.
Arroje un error si al intentar retirar dinero, el retiro haría que el balance quede debajo del min_balance. Es decir que sí se pueden hacer retiros siempre y cuando el balance quede arriba del min_balance.
"""

class BankAccount:
    def __init__(self, amount=0):
        self.balance = amount
    def _validate_amount(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("El monto debe ser numérico")
        if amount <= 0:
            raise ValueError("El monto debe ser mayor a 0")
    def deposit(self, amount):
        self._validate_amount(amount)
        self.balance += amount
    def withdraw(self, amount):
        self._validate_amount(amount)
        self.balance -= amount

class SavingsAccount(BankAccount):
    def __init__(self,min_amount, amount=0):
        super().__init__(amount)
        self.min_balance = min_amount
    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            raise ValueError("No puede retirar esa cantidad, el balance seria menor al minimo")
        super().withdraw(amount)
    