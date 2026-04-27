"""
Cree una clase LinkedList con los métodos:
insert_front(data): Inserta al inicio
insert_back(data): Inserta al final
delete(data): Elimina el primer nodo con el valor dado
print_all(): Imprime todos los valores
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.front = None
        self.back = None
#Inicio A B C FINAL
# FRONT A B C BACK     
    def insert_front(self, data):
        new_node = Node(data)
        if self.front is None:
            self.front = self.back = new_node
            return
        new_node.next = self.front
        self.front = new_node

    def insert_back(self, data):
        new_node = Node(data)
        if self.back is None:
            self.front = self.back = new_node
            return
        self.back.next = new_node
        self.back = new_node

    def delete(self, data):
        current = self.front
        previous = None
        while current:
            if current.data == data:
                if previous is None:  # Deleting the front node
                    self.front = current.next
                else:
                    previous.next = current.next
                if current == self.back:  # Deleting the back node
                    self.back = previous
                return
            previous = current
            current = current.next

    def print_all(self):
        current = self.front
        nodes = ""
        while current:
            nodes += current.data + " "
            current = current.next
        print(f"LINKED LIST: [{nodes.strip()}]")

linked_list = LinkedList()  
linked_list.insert_back("A")
linked_list.insert_back("B")
linked_list.insert_back("C")
linked_list.print_all()
linked_list.insert_front("D")
linked_list.print_all()
linked_list.delete("B")
linked_list.print_all()