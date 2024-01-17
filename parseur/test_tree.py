from anytree import Node, RenderTree, PreOrderIter

def remove_duplicate_children(node):
    # ajout d'un dictionnaire pour compter les children qui ont le meme père
    count_children = {}
    for parent in PreOrderIter(node):
        count_children[parent] = {}
        for child in parent.children:
            if child.name not in count_children[parent]:
                count_children[parent][child.name] = child
            else: # On ajoute les enfants du noeud qu'on supprime
                count_children[parent][child.name].children += child.children
                child.parent = None


root = Node("Root")
child1 = Node("Child1", parent=root)
child2 = Node("Child2", parent=root)
child3 = Node("Child1", parent=child1)
child4 = Node("Child1", parent=child1)
child5 = Node("Child2", parent=child4)
child6 = Node("Child2", parent=child4)
child7 = Node("Child7", parent=child5)


print("Before removing duplicate children:")
for pre, fill, node in RenderTree(root):
    print(f"{pre}{node.name}")


remove_duplicate_children(root)


print("\nAfter removing duplicate children:")
for pre, fill, node in RenderTree(root):
    print(f"{pre}{node.name}")



root2 = Node("Root")
child10 = Node("Child1", parent=root2)
child20 = Node("Child2", parent=root2)
child30 = Node("Child1", parent=None)
child40 = Node("Child1", parent=child10)
child50 = Node("Child2", parent=child40)
child60 = Node("Child2", parent=None)
child70 = Node("Child7", parent=child50)

print("\nI actually wanted:")
for pre, fill, node in RenderTree(root2):
    print(f"{pre}{node.name}")