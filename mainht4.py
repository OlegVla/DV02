#Конечно! В Python граф можно представить с помощью различных структур данных.
# Один из наиболее распространенных способов - это использование списка смежности.
# В этом случае граф представляется в виде словаря, где ключи - это вершины, а значения -
# это списки смежных вершин. Ниже приведен пример реализации графа с использованием
# списка смежности:

class Graph:
    def __init__(self):
        self.graph = {}

    # Метод для добавления вершины в граф
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    # Метод для добавления ребра в граф
    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)

        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  # Если граф неориентированный

    # Метод для отображения графа
    def display(self):
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")


# Пример использования
if __name__ == "__main__":
    g = Graph()

    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")

    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "C")
    g.add_edge("C", "D")

    g.display()

#В этом примере:
# #1. `Graph` - это класс, который представляет граф.
# 2. Метод `add_vertex` добавляет вершину в граф.
# 3. Метод `add_edge` добавляет ребро между двумя вершинами.
# Если граф неориентированный, то добавляются обе связи(от `vertex1` к `vertex2` и обратно).
# 4. Метод `display` отображает структуру графа .  Запустив приведенный код, вы получите
#вывод, показывающий структуру графа:
#A -> ['B', 'C']
#B -> ['A', 'C']
#C -> ['A', 'B', 'D']
#D -> ['C']
#Этот вывод показывает, как вершины связаны друг с другом.