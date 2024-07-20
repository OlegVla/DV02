#Чтобы вывести дерево на печать, можно использовать несколько подходов.
# Один из наиболее распространенных способов — это выполнение обхода дерева.
# В данном случае я покажу вам три способа обхода: прямой (pre-order),
# центрированный (in-order) и обратный (post-order).

#Добавим методы обхода дерева и функцию для печати дерева в ваш код:


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Функция для добавления нового узла
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# Прямой обход дерева (pre-order)
def print_pre_order(root):
    if root:
        print(root.val, end=' ')
        print_pre_order(root.left)
        print_pre_order(root.right)

# Центрированный обход дерева (in-order)
def print_in_order(root):
    if root:
        print_in_order(root.left)
        print(root.val, end=' ')
        print_in_order(root.right)

# Обратный обход дерева (post-order)
def print_post_order(root):
    if root:
        print_post_order(root.left)
        print_post_order(root.right)
        print(root.val, end=' ')

# Пример использования
root = Node(50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print("Прямой обход дерева (pre-order):")
print_pre_order(root)
print("\nЦентрированный обход дерева (in-order):")
print_in_order(root)
print("\nОбратный обход дерева (post-order):")
print_post_order(root)


#Этот код добавляет три функции для выполнения различных типов обхода дерева и печати значений узлов:

#1. `print_pre_order(root)`: Выполняет прямой (pre-order) обход, при котором обрабатывается текущий узел,
# затем левое поддерево, затем правое поддерево.
#2. `print_in_order(root)`: Выполняет центрированный (in-order) обход, при котором обрабатывается
# левое поддерево, затем текущий узел, затем правое поддерево. Этот метод особенно полезен для двоичных
# деревьев поиска (BST), так как он выводит значения в отсортированном порядке.
#3. `print_post_order(root)`: Выполняет обратный (post-order) обход, при котором обрабатывается левое
# поддерево, затем правое поддерево, затем текущий узел.

#Результатом выполнения этих функций будет печать значений узлов дерева в различных порядках обхода.