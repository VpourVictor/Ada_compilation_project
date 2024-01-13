import matplotlib.pyplot as plt
import networkx as nx
from anytree import Node, RenderTree

def plot_tree(tree, parent_name, graph, pos=None, level=0,
              width=2., vert_gap=0.4, xcenter=0.5):
    if pos is None:
        pos = {parent_name: (xcenter, 1 - level * vert_gap)}
    else:
        pos[parent_name] = (xcenter, 1 - level * vert_gap)
    children = tree.children(parent_name)
    if children:
        dx = width / 2
        nextx = xcenter - width / 2 - dx / 2
        for child in children:
            nextx += dx
            pos = plot_tree(tree, child.name, graph=graph, pos=pos,
                            level=level + 1, width=dx, xcenter=nextx)
    return pos

def draw_tree(tree):
    graph = tree

    pos = plot_tree(tree, tree.name, graph=graph)
    nx.draw(graph, pos=pos, with_labels=True, arrows=True)
    plt.show()

# Example Usage
if __name__ == "__main__":
    # Create a sample binary tree using anytree
    root = Node("Root")
    node1 = Node("Node1", parent=root)
    node2 = Node("Node2", parent=root)
    node3 = Node("Node3", parent=node1)
    node4 = Node("Node4", parent=node1)

    # Display the tree
    draw_tree(root)
