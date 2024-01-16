from anytree import Node, RenderTree, AsciiStyle, search, find_by_attr, PreOrderIter

# Create a tree structure
root = Node("Root")
child1 = Node("Child1", parent=root)
child2 = Node("Child2", parent=root)
child4 = Node("Child4", parent=root)
child3 = Node("Child3", parent=child2)
child5 = Node("1 C", parent = child1)


A = Node("A", parent=child3)
B = Node("B", parent=A)
C = Node("C", parent=B)
D  = Node("D", parent=B)

print("child2 name" ,child2.name)

C.parent=None

# Number of edges on the longest path to a leaf Node
print("Root height ", root.height)
print("D height ", D.height)
# Number of edges on the longest path to a root Node
print("Root deapth ", root.depth)
# Tree size — the number of nodes in tree starting at this node.
print("B.size ", B.size)
print("D.size", D.size)

print("descendants : " , child3.descendants)
print("siblings :  " , child2.siblings)
print("child1.is_leaf", child1.is_leaf)
print("D.is_leaf", B.is_leaf)
A.parent=child2


for node in D.iter_path_reverse():
    print(node)




result = search.findall(root, filter_=lambda node: node.name in ("C", "B"))
print(result)

#print([list(leaf.path) for leaf in PreOrderIter(root, filter_=lambda node: node.is_leaf)])

print(list(PreOrderIter(root, filter_=lambda node: node.is_leaf)))

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
