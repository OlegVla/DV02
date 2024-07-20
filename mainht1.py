#Конечно! Вот пример программы на языке Python, которая реализует стек с помощью списка:
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


# Пример использования стека
if __name__ == "__main__":
    stack = Stack()
    print("Стек пуст?", stack.is_empty())

    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Стек после добавления элементов:", stack)

    print("Верхний элемент стека:", stack.peek())
    print("Размер стека:", stack.size())

    print("Извлеченный элемент:", stack.pop())
    print("Стек после извлечения элемента:", stack)

    print("Верхний элемент стека:", stack.peek())
    print("Размер стека:", stack.size())

    print("Стек пуст?", stack.is_empty())


#Этот код определяет класс `Stack`, который представляет собой стек и содержит
# методы для выполнения основных операций со стеком: добавление элемента(`push`),
# извлечение элемента(`pop`), просмотр верхнего элемента(`peek`), проверка на
# пустоту(`is_empty`), получение размера стека(`size`) и преобразовани стека в строку
# (`__str__`).В основной части программы показан пример использования этого класса.