#Конечно! Реализация дерева(например, бинарного дерева) на языке Python с
# использованием списков может быть выполнена разными способами.
# дин из подходо  заключается в том, чтобы использовать вложенные
# списки для представления узлов и поддеревьев. Вот пример простой
# реализации бинарного дерева:

class BinaryTree:
    def __init__(self, root_value):
        self.tree = [root_value, [], []]

    def insert_left(self, new_value):
        left_subtree = self.tree.pop(1)
        if len(left_subtree) > 1:
            self.tree.insert(1, [new_value, left_subtree, []])
        else:
            self.tree.insert(1, [new_value, [], []])

    def insert_right(self, new_value):
        right_subtree = self.tree.pop(2)
        if len(right_subtree) > 1:
            self.tree.insert(2, [new_value, [], right_subtree])
        else:
            self.tree.insert(2, [new_value, [], []])

    def get_root_value(self):
        return self.tree[0]

    def get_left_child(self):
        return self.tree[1]

    def get_right_child(self):
        return self.tree[2]

    def __str__(self):
        return str(self.tree)


# Пример использования бинарного дерева
if __name__ == "__main__":
    bt = BinaryTree(1)
    print("Дерево после создания корня:", bt)

    bt.insert_left(2)
    print("Дерево после вставки 2 в левое поддерево:", bt)

    bt.insert_right(3)
    print("Дерево после вставки 3 в правое поддерево:", bt)

    left_child = bt.get_left_child()
    print("Левый ребенок корня:", left_child)

    right_child = bt.get_right_child()
    print("Правый ребенок корня:", right_child)


#В этой реализации: - `BinaryTree` представляет собой бинарное дерево,
# где каждый узел представлен списком из трех элементов:
# значение узла, левое поддерево и правое поддерево. - Метод `insert_left`
# вставляет новый узел в левое поддерево. - Метод `insert_right` вставляет
# новый узел в  правое поддерево. - Метод `get_root_value` возвращает значение
# корневого узла. - Методы `get_left_child` и `get_right_child` возвращают
# соответственно левое и правое поддеревья. Пример использовани
# показывает, как можно  создать дерево, добавить в него элементы и получить
# доступ к его узлам.