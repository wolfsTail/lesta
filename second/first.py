"""
 FIFO на основе двусвязного списка. Неограничена.
"""


class Node:
    """
    Элемент очереди на базе связного списка.
    """
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

    def __str__(self):
        return str(self.value)


class FIFO:
    """
    Очередь на базе двунаправленного связного списка.
    Имеет два указателя на начало и конец очереди, для корректной реализации
    FIFO буфера.
    """

    def __init__(self):
        self.top = Node(None)
        self.tail = self.top

    def enqueue(self, value):
        """
        Добавляет элемент с значением value в конец очереди.
        """
        new_node = Node(value)

        if self.top.next_node is None:
            self.top.next_node = new_node
            new_node.prev_node = self.top
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node

        return None

    def dequeue(self):
        """
        Извлекает элемент из начала очереди.
        """
        if not self.top.next_node:
            return None

        first = self.top.next_node
        self.top.next_node = first.next_node

        if first.next_node:
            first.next_node.prev_node = self.top
        else:
            self.tail = self.top

        return first.value
    