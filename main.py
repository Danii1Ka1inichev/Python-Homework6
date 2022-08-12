from abc import ABC, abstractmethod
import settings
import grafviz


settings.init()


class Node(ABC):


    def iter_tree(node):
        print(node.info)
        if node.edge:
            for i in node.edge:
                i.iter_tree()
        if not node.edge:
            return
    # def __iter__(self):

    @abstractmethod
    def __init__(self, info, name):
        self.name = name
        self.info = info
        self.edge = []
        settings.list_of_nodes.append(self)

    def add_edge(self, other):
        self.edge.append(other)
        settings.list_of_edges.append(f'{self.name}{other.name}')
        # self.edge.append({other: self})


class Number(Node):
    def __init__(self, info: int, name):
        super().__init__(info, name)


class String(Node):
    def __init__(self, info: str, name):
        super().__init__(info, name)


x = String('Cтихотворения "Мир за гранью" ', 'x')
a = String('Кружась, сияет вихрь реальности и снов,', 'a')
b = Number(1, 'b')
b.add_edge(a)
c = String('Вселенная живёт, творя и вновь губя.', 'c')
d = Number(2, 'd')
d.add_edge(c)
e = String('У космоса есть много голосов,', 'e')
f = Number(3, 'f')
f.add_edge(e)
g = String('Он полон тайн. И он зовёт тебя.', 'g')
h = Number(4, 'h')
h.add_edge(g)

x.add_edge(b)
x.add_edge(d)
x.add_edge(f)
x.add_edge(h)


grafviz.draw_graf()

x.iter_tree()