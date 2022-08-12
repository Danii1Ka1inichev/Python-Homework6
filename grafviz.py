from graphviz import Digraph
import settings


def draw_graf():
    nodes = settings.list_of_nodes
    edges = settings.list_of_edges
    dot = Digraph(comment='Poem')
    add_node(dot, nodes)
    dot.view()
    dot.edges(edges)
    print(dot.source)
    # dot.view()
    dot.render('Folder/Poem.gv', view=True)


def add_node(dot, nodes):
    for i in range(len(nodes)):
        dot.node(nodes[i].name, f'Dot {nodes[i].info}')


