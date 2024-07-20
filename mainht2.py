#Конечно! Вот пример программы  на языке Python, которая реализует
#очередь с помощью списка:
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


# Пример использования очереди
if __name__ == "__main__":
    queue = Queue()
    print("Очередь пуста?", queue.is_empty())

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Очередь после добавления элементов:", queue)

    print("Первый элемент в очереди:", queue.front())
    print("Размер очереди:", queue.size())

    print("Извлеченный элемент:", queue.dequeue())
    print("Очередь после извлечения элемента:", queue)

    print("Первый элемент в очереди:", queue.front())
    print("Размер очереди:", queue.size())

    print("Очередь пуста?", queue.is_empty())


#Этот код определяет класс `Queue`, который представляет собой очередь и содержит
# методы для выполнения основных операций с очередью: добавление элемента в конец
# (`enqueue`), извлечение элемента из начала(`dequeue`), просмотр первого
# элемента(`front`), проверка на пустоту(`is_empty`), получение размера очереди(`size`) и
# преобразование очереди в строку(`__str__`).В основной части программы показан пример
# использования этого класса.