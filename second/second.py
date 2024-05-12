"""
    FIFO на основе статического масива.
"""


class FIFO:
    def __init__(self, n: int):
        self.size = n + 1
        self.data = [None] * self.size
        self.head = 0
        self.tail = 0

    def enqueue(self, value):
        """
        Добавляет элемент в конец очереди.
        """
        next_idx = (self.tail + 1) % self.size
        if next_idx == self.head:
            raise IndexError("Буфер полон")
        self.data[self.tail] = value
        self.tail = next_idx
        return None

    def dequeue(self):
        """
        Возвращает элемент из начала очереди, если такой элемент
        существует.
        """
        if self.head == self.tail:
            return None
        item = self.data[self.head]
        self.head = (self.head + 1) % self.size
        return item
