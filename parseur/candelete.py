from anytree import Node, RenderTree, AsciiStyle, search, find_by_attr, PreOrderIter

# Create a tree structure
root = Node("Root")
child1 = Node("Child1", parent=root)
child2 = Node("Child2", parent=root)
child4 = Node("Child4", parent=root)
child3 = Node("Child3", parent=child2)
child5 = Node("1 C", parent=child1)
child9 = Node("1 C", parent=root)

A = Node("A", parent=child3)
B = Node("B", parent=A)
C = Node("C", parent=B)
D = Node("D", parent=B)

# print("child2 name" ,child2.name)

C.parent = None


# # Number of edges on the longest path to a leaf Node
# print("Root height ", root.height)
# print("D height ", D.height)
# # Number of edges on the longest path to a root Node
# print("Root deapth ", root.depth)
# # Tree size — the number of nodes in tree starting at this node.
# print("B.size ", B.size)
# print("D.size", D.size)
#
# print("descendants : " , child3.descendants)
# print("siblings :  " , child2.siblings)
# print("child1.is_leaf", child1.is_leaf)
# print("D.is_leaf", B.is_leaf)
# A.parent=child2
#
#
# for node in D.iter_path_reverse():
#     print(node)

# L = child2.children
def supprimer_noeuds_un_seul_fils(node):
    children = node.children
    if len(children) == 1:
        # if len(children) == 1 and not children[0].is_leaf:
        # Si le nœud a un seul fils qui n'est pas une feuille, le supprimer
        parent = node.parent
        node.parent = None  # Cela supprime le nœud de son parent
        children[0].parent = parent
        return True
    return False


def remove_duplicate_parent_links(node):
    children = node.children
    l = len(children)

    if l == 2 and children[0].name == children[1].name :
        if children[0].is_leaf :
            children[0].parent = None
        else :
            children[1].parent = None
        return True

    elif l > 1:

        L = []
        for i in range(0, l):
            L.append(children[i].name)
        j = 0
        nb_of_del = 0
        while j != l - 1 :
            if children[j+nb_of_del].name in (L[:j] + L[j + 1:]):
                nb_of_del += 1
                children[j+nb_of_del].parent = None
                l -= 1
                del L[j]
            j += 1
        if nb_of_del != 0 :
            return True

    return False



#
# result = search.findall(root, filter_=lambda node: node.name in ("C", "B"))
# print(result)
#
# print([list(leaf.path) for leaf in PreOrderIter(root, filter_=lambda node: node.is_leaf)])
#
# print(list(PreOrderIter(root, filter_=lambda node: node.is_leaf)))
print("Avant la suppression:")
for pre, fill, node in RenderTree(root):
    print(f"{pre}{node.name}")


def delete_all_nodes(root):
    for node in PreOrderIter(root):
        if supprimer_noeuds_un_seul_fils(node):
            delete_all_nodes(root)


def delete_all_duplicates(root):
    for node in PreOrderIter(root):
        if remove_duplicate_parent_links(node):
            delete_all_duplicates(root)


delete_all_nodes(root)

# Display the tree structure
print("Après la suppression:")
for pre, _, node in RenderTree(root):
    print(f"{pre}{node.name}")

delete_all_duplicates(root)
D.parent=None
child4.parent=None
child8 = Node("1 C", parent=root)
delete_all_duplicates(root)

print("Après le dédoublage:")
for pre, _, node in RenderTree(root):
    print(f"{pre}{node.name}")

# If you want a graphical representation (requires Graphviz)
try:
    from anytree.exporter import DotExporter

    DotExporter(root).to_picture("tree.png")
    print("Tree visualization saved as tree.png")
except ImportError:
    print("Graphviz not installed. Unable to create graphical representation.")
