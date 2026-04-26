"""
Lista doblemente enlazada
Requisitos:
Cada nodo debe tener referencia al siguiente y al anterior
Métodos:
append(data): Agrega al final
prepend(data): Agrega al inicio
delete(data): Elimina el primer nodo con ese valor
print_forward() y print_backward(): Imprime en ambas direcciones
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.front = None
        self.back = None

    def append(self, data):
        new_node = Node(data)
        if self.back is None:
            self.front = self.back = new_node
            return
        self.back.next = new_node
        new_node.prev = self.back
        self.back = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.front is None:
            self.front = self.back = new_node
            return
        new_node.next = self.front
        self.front.prev = new_node
        self.front = new_node

    def delete(self, data):
        current = self.front
        while current:
            if current.data == data:
                #Si hay previo lo vincula al sigueinte
                if current.prev:
                    current.prev.next = current.next
                #Si no, entonces el siguiente se vuelve el nuevo frente
                else:
                    self.front = current.next
                #Si hay siguiente lo vincula al previo
                if current.next:
                    current.next.prev = current.prev
                #Si no, entonces el previo se vuelve el nuevo final
                else:
                    self.back = current.prev
                return
            current = current.next

    def print_forward(self):
        current = self.front
        nodes = ""
        while current:
            nodes += current.data + " "
            current = current.next
        print(f"FORWARD: [{nodes.strip()}]")

    def print_backward(self):
        current = self.back
        nodes = ""
        while current:
            nodes += current.data + " "
            current = current.prev
        print(f"BACKWARD: [{nodes.strip()}]")

double_linked_list = DoubleLinkedList()
double_linked_list.append("A")
double_linked_list.append("B")
double_linked_list.append("C")
double_linked_list.print_forward()
double_linked_list.print_backward()
double_linked_list.prepend("X")
double_linked_list.print_forward()
double_linked_list.print_backward()
double_linked_list.delete("B")
double_linked_list.print_forward()