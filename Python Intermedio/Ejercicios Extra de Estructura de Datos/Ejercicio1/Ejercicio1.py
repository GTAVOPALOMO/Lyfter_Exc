"""
Cree una estructura que represente una cola básica (Queue) con objetos enlazados
Restricción:
no usar list, dict, tuple, collections
Métodos requeridos:
enqueue(data): agrega un nodo al final
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.front is None:
            self.rear = self.front = new_node
            return
        self.front.next = new_node
        self.front = new_node

    def dequeue(self):
        if self.rear is None:
            return None
        temp = self.rear
        self.rear = temp.next
        if self.rear is None:
            self.front = None
        return temp.data
    
    def print_all(self):
        current = self.rear
        nodes = ""
        while current:
            nodes += current.data + " "
            current = current.next
        print(f"QUEUE: [{nodes.strip()}]")
        
queue = Queue()

queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")

queue.print_all()
print(f"DEQUEUED: {queue.dequeue()}")  
print(f"DEQUEUED: {queue.dequeue()}")  
print(f"DEQUEUED: {queue.dequeue()}")  
print(f"DEQUEUED: {queue.dequeue()}") 