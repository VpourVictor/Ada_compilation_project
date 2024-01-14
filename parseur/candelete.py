from anytree import Node, RenderTree

# Create a tree structure
root = Node("Root")
child1 = Node("Child1", parent=root)
child2 = Node("Child2", parent=root)
child2 = Node("Child4", parent=root)
child3 = Node("Child3", parent=child2)

# Display the tree structure
for pre, _, node in RenderTree(root):
    print(f"{pre}{node.name}")

# If you want a graphical representation (requires Graphviz)
try:
    from anytree.exporter import DotExporter
    DotExporter(root).to_picture("tree.png")
    print("Tree visualization saved as tree.png")
except ImportError:
    print("Graphviz not installed. Unable to create graphical representation.")
