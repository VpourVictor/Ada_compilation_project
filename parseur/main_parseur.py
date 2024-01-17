from anytree import Node, RenderTree, search, PreOrderIter, PostOrderIter
from anytree.exporter import DotExporter

import lexeur.file_to_code_ter as file
import parseur.functions

dico_N = {"N9": "instruction"}


def generate_tree(name_file):
    try:
        DotExporter(root).to_picture(filename=name_file)
        print("Tree visualization saved")
    except ImportError:
        print("Graphviz not installed. Unable to create graphical representation.")


def delete_leef_eps(racine):
    for node in racine.leaves:
        if isDelete(node.name):
            node.parent = None


def delete_leef_epsX(racine):
    for i in range(0, racine.height):
        delete_leef_eps(racine)


def isDelete(name):
    nom = name.split(" ")
    return nom[1][0].isupper() or nom[1] in [".", ",", "(", ")", ";", "is", "begin", "with", "id(Ada)", "id(Text_IO)", "use"]


def supprimer_noeuds_un_seul_fils(node):
    children = node.children
    if len(children) == 1 :
        #if len(children) == 1 and not children[0].is_leaf:
        # Si le nœud a un seul fils qui n'est pas une feuille, le supprimer
        parent = node.parent
        node.parent = None  # Cela supprime le nœud de son parent
        children[0].parent = parent
        return True
    return False


def remove_duplicate_parent_links(node):
    children = node.children
    l = len(children)

    if l == 2 and children[0].name == children[1].name:
        if children[0].is_leaf:
            children[0].parent = None
        else:
            children[1].parent = None
        return True

    elif l > 1:

        L = []
        for i in range(0, l):
            L.append(children[i].name)
        j = 0
        nb_of_del = 0
        while j != l - 1:
            if children[j + nb_of_del].name in (L[:j] + L[j + 1:]):
                nb_of_del += 1
                children[j + nb_of_del].parent = None
                l -= 1
                del L[j]
                j -= 1
            j += 1
        if nb_of_del != 0:
            return True

    return False


def remove_duplicate_children_working(node):
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


def delete_all_duplicates(root):
    for node in PreOrderIter(root):
        if remove_duplicate_parent_links(node):
            delete_all_duplicates(root)


def supprimer_Expr(node):
    name = node.name.split(" ")
    if name[1][0] == "E":
        children = node.children
        parent = node.parent
        node.parent = None  # Cela supprime le nœud de son parent
        for i in range(len(node.children)):
            children[i].parent = parent
        return True


def delete_all_nodes(root):
    for node in PreOrderIter(root):
        if supprimer_noeuds_un_seul_fils(node):
            delete_all_nodes(root)


def operation(node):
    op = ["+", "-", "*", "/"]
    for i in range(0, len(node.children)):
        # si un noeud à un enfant qui est un opérateur
        name = node.children[i].name.split(" ")
        if name[1] in op:
            # les frères de l'opérateur deviennent les enfants du père du noeud
            freres = node.children[i].siblings
            for j in range(0, len(freres)):
                freres[j].parent = node.parent
            # on change le nom du père du noeud par le nom de l'opérateur
            node.parent.name = name[0] + " " + name[1]
            # on supprime le noeud
            node.parent = None
            break


def addBlockNode(node):
    name = node.name.split(" ")
    x = Node(name[0]+" BLOCK", node.parent)
    node.parent = x
    return x


def clean(node):
    children = node.children
    for j in range(0, len(children)-1):
        for i in range(j+1,len(children)):
            if int(children[j].name.split(" ")[0])> int(children[i].name.split(" ")[0]):
                children[j].parent = None
                children[j].parent = node


def removeA2(node):
    for node in PreOrderIter(node):
        if node.name != "N1":
            name = node.name.split(" ")
            if name[1] == "A2":
                addBlockNode(node)
                A2_destroyer(node)


def cas_difference(node):
    if node.name.split(" ")[1] == "condExpr":
        print("dfnkdsnkjnskjnfkdsnfdslknflkdsnflkdsnflkdsnflkdsnfdlksndsnflkdsnf")
        children = node.children
        for i in range(0, len(children)):
            name = children[i].name.split(" ")
            if name[1] == "/":
                enfant = children[i].children
                for j in range(0, len(enfant)):
                    if enfant[j].name.split(" ")[1] != "=":
                        enfant[j].parent = node

        for i in range(0, len(children)):
            name = children[i].name.split(" ")
            if name[1] == "/":
                children[i].parent = None

        node.name = node.name.split(" ")[0] + " " + "/="


def generate_final_AST(root):
    delete_leef_epsX(root)
    delete_all_nodes(root)
    remove_duplicate_children_working(root)
    boucle_node(root)
    test_logique(root)
    A2counter = 0
    for node in PreOrderIter(root):
        if node.name != "N1":
            name = node.name.split(" ")
            if name[1] == "instruction":
                for i in range(0, len(node.children)):
                    name = node.children[i].name.split(" ")
                    if name[1] == "return":
                        return_instr(node)
                    elif name[1] == "N92":
                        affect(node)
            if name[1] == "A2":
                A2counter +=1
    for i in range(A2counter):
        removeA2(root)
    clean(root)
    h = hauteur_arbre(root)
    for i in range(h):
        for node in PostOrderIter(root):
            clean(node)

    for node in PreOrderIter(root):
        if node.name != "N1":
            operation(node)

    for i in range(0, 2):
        for node in PreOrderIter(root):
            if node.name != "N1":
                name = node.name.split(" ")
                if name[1][:4] == "EXPR":
                    operation(node)

    for i in range(0, 5):
        for node in PreOrderIter(root):
            if node.name != 'N1':
                supprimer_Expr(node)

    for node in PreOrderIter(root):
        if node.name != "N1":
            delete_node(node)

    remove_duplicate_children_working(root)

    for node in PreOrderIter(root):
        if node.name != "N1":
            operationCond(node)

    for node in PreOrderIter(root):
        if node.name != "N1":
            cas_difference(node)

    remove_duplicate_children_working(root)

    return root


def hauteur_arbre(root):
    return max(node.depth for node in PreOrderIter(root))


def reduce_ope3(node):
    node_nom = node.name.split(" ")
    if node_nom[1] == "condExpr":
        # on récupère dans un tableau les noms des 3 fils
        name = [node.children[0].name.split(" ")[1], node.children[1].name.split(" ")[1],
                node.children[2].name.split(" ")[1]]
        # si le fils du milieu est un opérateur
        tab_ope = ["+", "-", "*", "/", ">", "<"]
        if node_nom[1] == "condExpr":
            tab_ope.append("=")
        if name[1] in tab_ope:
            # on récupère les 2 fils du milieu
            children = [node.children[0], node.children[2]]
            # on supprime le noeud du milieu
            node.children[1].parent = None
            # on ajoute les 2 fils du milieu au noeud parent
            for i in range(len(children)):
                children[i].parent = node
            # on renomme le noeud parent
            node.name = node.name.split(" ")[0] + " " + name[1]


def reduce_ope4(node):
    node_nom = node.name.split(" ")
    if node_nom[1] == "condExpr":
        # on récupère dans un tableau les noms des 4 fils
        name = [node.children[0].name.split(" ")[1], node.children[1].name.split(" ")[1],
                node.children[2].name.split(" ")[1], node.children[3].name.split(" ")[1]]
        # on concatène les noms des 2 fils du milieu
        ope = name[1] + "" + name[2]
        # si le fils du milieu est un opérateur
        tab_ope = ["<=", ">=", "/="]
        if ope in tab_ope:
            # on récupère les 2 filsà garder
            children = [node.children[0], node.children[3]]
            # on supprime les 2 fils du milieu
            node.children[2].parent = None
            node.children[1].parent = None
            # on ajoute les 2 fils du milieu au noeud parent
            for i in range(len(children)):
                children[i].parent = node
            # on renomme le noeud parent
            node.name = node.name.split(" ")[0] + " " + ope


def operationCond(node):
    if len(node.children) == 3:
        reduce_ope3(node)
    # si le noeud à 4 fils
    elif len(node.children) == 4:
        reduce_ope4(node)


def countleaves(node):
    return sum(1 for _ in PreOrderIter(node, filter_=lambda x: x.is_leaf))


def rename(node):
    name = node.name.split(" ")
    if name[1] in dico_N.keys():
        node.name = name[0] + " " + dico_N[name[1]]


def affect(node):
    name = node.name.split(" ")
    node.name = name[0] + " " + "affect :="
    for i in range(0, len(node.children)):
        name = node.children[i].name.split(" ")
        if name[1] == "N92":
            list_children = node.children[i].children
            node.children[i].name = node.children[i].children[len(node.children[i].children) - 1].name
            node.children[i].children = list_children[len(node.children[i].children) - 1].children


def return_instr(node):
    name = node.name.split(" ")
    node.name = name[0] + " " + "return"
    for i in range(0, len(node.children)):
        name = node.children[i].name.split(" ")
        if name[1] == "N8":
            list_children = node.children[i].children
            node.children[i].name = node.children[i].children[len(node.children[i].children) - 1].name
            node.children[i].children = list_children[len(node.children[i].children) - 1].children


def delete_node(node):
    name = node.name.split(" ")
    if name[1] == "N8":
        children = node.children
        for i in range(len(children)):
            children[i].parent = node.parent
            node.parent = None
    for i in range(0, len(node.children)):
        name = node.children[i].name.split(" ")
        if name[1] == "return":
            node.children[i].parent = None
            break




def boucle_node(root):
    for node in PreOrderIter(root):
        if node.name != "N1":
            rename(node)


def A2_destroyer(root):

    children = root.children
    for i in range(len(children)):
        nameChildren = children[i].name.split(" ")
        if nameChildren[1] == "A2":
            A2_destroyer(children[i])
    children = root.children
    for j in range(len(children)):
        children[j].parent = root.parent
    root.parent = None

def test_logique(root):
    for node in PreOrderIter(root):
        test_if(node, "BLOCK")
        test_elsif(node, "BLOCK")
        test_else(node, "BLOCK")


def test_if(node, string):
    if node.name != "N1":
        name = node.name.split(" ")[1]
        if name == "if":
            sibling = node.siblings
            for i in range(0, len(sibling)):
                nameS = sibling[i].name.split(" ")
                if (nameS[1] == "N8"):
                    sibling[i].name = nameS[0] + " " + "condExpr"
                    sibling[i].parent = node
                    break
            sibling = node.siblings
            for i in range(0, len(sibling)):
                nameS = sibling[i].name.split(" ")
                if nameS[1] == "then":
                    sibling[i].parent = None
                    break
            sibling = node.siblings
            for i in range(0, len(sibling)):
                nameS = sibling[i].name.split(" ")
                if(nameS[1] == "instruction"):
                    x = Node(nameS[0] + " BLOCK", node)
                    sibling[i].parent = x
                    break
                if(nameS[1] == "A2"):
                    x = addBlockNode(sibling[i])
                    x.parent = node
                    A2_destroyer(sibling[i])
                    break
            sibling = node.siblings
            for i in range(0, len(sibling)):
                nameS = sibling[i].name.split(" ")[1]
                nameS2 = sibling[i + 1].name.split(" ")[1]
                if nameS == "end" and nameS2 == "if":
                    sibling[i].parent = None
                    sibling[i + 1].parent = None
                    break



def test_elsif(node, string):
    if node.name != "N1":
        name = node.name.split(" ")[1]
        if name == "elsif":
            sibling = node.siblings
            for i in range(0, len(sibling)):
                nameS = sibling[i].name.split(" ")
                if nameS[1] == "N8":
                    sibling[i].name = nameS[0] + " " + "condExpr"
                    sibling[i].parent = node
                    break
            sibling = node.siblings
            for i in range(0, len(sibling)):
                nameS = sibling[i].name.split(" ")
                if nameS[1] == "then":
                    sibling[i].parent = None
                    break
            sibling = node.siblings
            for i in range(0, len(sibling)):
                nameS = sibling[i].name.split(" ")

                if(nameS[1] == "instruction"):
                    x = Node(nameS[0] + " BLOCK", node)
                    sibling[i].parent = x
                    break
                if(nameS[1] == "A2"):
                    x = addBlockNode(sibling[i])
                    x.parent = node
                    A2_destroyer(sibling[i])
                    break
            temp = node.parent.parent
            node.parent.parent = None
            node.parent = temp

def test_else(node, string):
    if node.name != "N1":
        name = node.name.split(" ")[1]
        if name == "else":
            sibling = node.siblings
            for i in range(0, len(sibling)):
                nameS = sibling[i].name.split(" ")
                if (nameS[1] == "instruction"):
                    x = Node(nameS[0] + " BLOCK", node)
                    sibling[i].parent = x
                    break
                if(nameS[1] == "A2"):
                    x = addBlockNode(sibling[i])
                    x.parent = node
                    A2_destroyer(sibling[i])
                    break
            temp = node.parent.parent
            node.parent.parent = None
            node.parent = temp

if __name__ == '__main__':
    print("On va maintenant tester notre parseur")
    print("Pour chaque test, on va afficher la liste de token renvoyé par le lexeur, puis générer l'arbre syntaxique "
          "associé")
    print("On va tester les exemples suivants :")
    print("On commence par un exemple simple : un programme qui se charge de faire une somme entre 2 entiers :")
    token_list = file.get_token("exemples/exemple_calcul.ada")
    print(token_list)
    root = Node('N1')
    print(parseur.functions.fonction_N1(token_list, root))
    generate_final_AST(root)
    generate_tree("tree_calcul.png")

    print("On va maintenant tester un exemple qui contient des procédures imbriquées :")
    token_list = file.get_token("exemples/exemple_double_procedure.ada")
    print(token_list)
    root = Node('N1')
    print(parseur.functions.fonction_N1(token_list, root))
    generate_final_AST(root)
    generate_tree("tree_double_procedure.png")

    print("On va maintenant tester un exemple qui contient blocs d'instructions if elif et else :")
    token_list = file.get_token("exemples/exemple_if_elif.ada")
    print(token_list)
    root = Node('N1')
    print(parseur.functions.fonction_N1(token_list, root))
    generate_final_AST(root)
    generate_tree("tree_if_elif.png")

    print("On va maintenant tester si notre parseur fonctionne avec un programme qui contient des if et des while :")
    token_list = file.get_token("exemples/exemple_if_while.ada")
    print(token_list)
    root = Node('N1')
    print(parseur.functions.fonction_N1(token_list, root))
    generate_final_AST(root)
    generate_tree("tree_if_while.png")

    print("Le test qui suit vise à montrer que l'on traite bien le cas où notre grammaire n'est pas LL1 (/=, /) :")
    token_list = file.get_token("exemples/exemple_division_difference.ada")
    print(token_list)
    root = Node('N1')
    print(parseur.functions.fonction_N1(token_list, root))
    generate_final_AST(root)
    generate_tree("tree_division_difference.png")

    print("On va maintenant tester un exemple qui tourne autour des expressions arithmétiques :")
    token_list = file.get_token("exemples/exemple_expression_arithmetique.ada")
    print(token_list)
    root = Node('N1')
    print(parseur.functions.fonction_N1(token_list, root))
    generate_final_AST(root)
    generate_tree("tree_expression_arithmetique.png")

    print("On va maintenant tester un exemple qui contient des fonctions imbriquées :")
    token_list = file.get_token("exemples/exemple_fonctions_imb.ada")
    print(token_list)
    root = Node('N1')
    print(parseur.functions.fonction_N1(token_list, root))
    generate_final_AST(root)
    generate_tree("tree_fonctions_imb.png")

    print("On va maintenant tester un exemple qui mélange un peut tout (fonctions, procédures) :")
    token_list = file.get_token("exemples/exemple_mixte.ada")
    print(token_list)
    root = Node('N1')
    print(parseur.functions.fonction_N1(token_list, root))
    generate_final_AST(root)
    generate_tree("tree_mixte.png")

    print("Le dernier test est effectué sur le code fournit dans le sujet :")
    token_list = file.get_token("exemples/exemple.ada")
    print(token_list)
    root = Node('N1')
    print(parseur.functions.fonction_N1(token_list, root))
    generate_final_AST(root)
    generate_tree("tree_exemple.png")

    token_list = file.get_token("exemples/exemple_erreur_ortho.ada")
    print(token_list)
    root = Node('N1')
    print(parseur.functions.fonction_N1(token_list, root))
    generate_final_AST(root)
    generate_tree("exemple_erreur_ortho.png")

    # Display the tree structure
    # for pre, _, node in RenderTree(root):
    #     print(f"{pre}{node.name}")
