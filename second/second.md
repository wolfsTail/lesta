## Реализация циклического буфера FIFO

### Двунаправленный связный список


``` python
class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

    def __str__(self):
        return str(self.value)


class FIFO:

    def __init__(self):
        self.top = Node(None)
        self.tail = self.top

    def enqueue(self, value):

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

        if not self.top.next_node:
            return None

        first = self.top.next_node
        self.top.next_node = first.next_node

        if first.next_node:
            first.next_node.prev_node = self.top
        else:
            self.tail = self.top

        return first.value

```

**Плюсы:**
-  Удаление и добавление элементов происходит за константное время O(1).
-  Размер буфера ограничен лишь пределами памяти устройства.

**Минусы:**
- Каждый элемент структуры, определен отдельным класом, который хранит данные, в том числе и на два указателя, что увеличивает общий объем используемой памяти.
- Объекты могут быть размещены в разных частях памяти, что может увеличить константу времени доступа к каждому конкртеному элементу.


### Реализация на базе статического массива

``` python
class FIFO:
    def __init__(self, n: int):
        self.size = n + 1
        self.data = [None] * self.size
        self.head = 0
        self.tail = 0

    def enqueue(self, value):
        next_idx = (self.tail + 1) % self.size
        if next_idx == self.head:
            raise IndexError("Буфер полон")
        self.data[self.tail] = value
        self.tail = next_idx
        return None

    def dequeue(self):
        if self.head == self.tail:
            return None
        item = self.data[self.head]
        self.head = (self.head + 1) % self.size
        return item
```

**Плюсы:**
- Более эффективное использование заранее выделенной памяти.
- Очевидность реализации циклической структуры массива.

**Минусы:**
- Ограниченный размер очереди. Требует дополнительной обработки ошибок связанных с переполнением.

### Лицом к лицу

#### Оценка скорости выполнения операция

Обе реализации обеспечивают константное время добавления и извлечения элемента. Однако, теоретически в реализации на базе статического массивы время доступа может быть более быстрым из-за более оптимальной организации структуры данных в памяти устройства.

#### Оценка затрачиваемой памяти

Реализация буфера на базе двусвязного списка требует больше памяти для хранения одного элемента, массив же более рационально использует память, но в ней ограничен.

### Резюме

Выбор подходящей реализации должен зависить от специфических требований к производительности и использованию памяти проектируемого приложения, а также предпочтений разработчика.
