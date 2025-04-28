class Stack:
    def __init__(self):
        #stack muss privat sein, damit nicht von außen die Datenstruktur manipuliert werden kann
        #nur über die öffentlich zugänglichen Methoden werden Stacks und Queues verändert
        self._stack = []

    def is_empty(self):
        return len(self._stack) == 0

    def size(self):
        return len(self._stack)

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self._stack.pop()
        #raise ist neu, Fehler wird direkt ausgegeben
        #Fehlerfall wird von normaler Logik getrennt
        raise IndexError("Pop von leerem Stack")

    def top(self):
        if not self.is_empty():
            #auch schon wieder verrückt: -1 verweist auf das letzte Element der Liste
            return self._stack[-1]
        raise IndexError("Top von leerem Stack")

# Queue-Klasse
class Queue:
    def __init__(self):
        self._queue = []

    def is_empty(self):
        return len(self._queue) == 0

    def size(self):
        return len(self._queue)

    def enqueue(self, item):
        self._queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self._queue.pop(0)
        raise IndexError("Dequeue von leerer Queue")

    def front(self):
        if not self.is_empty():
            return self._queue[0]
        raise IndexError("Front von leerer Queue")