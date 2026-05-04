"""
Cree una estructura de objetos que asemeje un Double Ended Queue.
Debe incluir los métodos de push_left y push_right (para agregar nodos al inicio y al final) y pop_left y pop_right (para quitar nodos al inicio y al final).
Debe incluir un método para hacer print de toda la estructura.
No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
class Deque:
    
    def __init__(self):
        self.left = None
        self.right = None
    
    def push_left(self, value):
        new_node = Node(value)
        if self.left is None:
            self.left = new_node
            self.right = new_node
        else:
            new_node.next = self.left
            self.left.prev = new_node
            self.left = new_node
    
    def push_right(self, value):
        new_node = Node(value)
        if self.right is None:
            self.left = new_node
            self.right = new_node
        else:
            new_node.prev = self.right
            self.right.next = new_node
            self.right = new_node
    
    def pop_left(self):
        if self.left is None:
            raise IndexError("La lista está vacía")
        value = self.left.value
        self.left = self.left.next
        if self.left is not None:
            self.left.prev = None
        else:
            self.right = None
        return value
    
    def pop_right(self):
        if self.right is None:
            raise IndexError("La lista está vacía")
        value = self.right.value
        self.right = self.right.prev
        if self.right is not None:
            self.right.next = None
        else:
            self.left = None
        return value
    
    def print_deque(self):
        current = self.left
        nodes = ""
        while current is not None:
            nodes += str(current.value) + " "
            current = current.next
        print(f"DEQUEUE: {nodes.strip()}")


deque = Deque()
deque.push_left("A")
deque.push_right(2)
deque.push_left(3.14)
deque.print_deque()
print("Pop left:", deque.pop_left())
print("Pop right:", deque.pop_right())
deque.print_deque()
