from anytree import Node, RenderTree, search, PreOrderIter
from anytree.exporter import DotExporter

import lexeur.file_to_code_ter as file
import parseur.functions

dico_N = {"N9": "instruction"}


# def delete_EXPR1(root):
#     for pre, _, node in RenderTree(root):
#         if "N9" in node.name :


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
        if node.name != 'N1':
            supprimer_Expr(node)

def generate_final_AST(root):
    delete_leef_epsX(root)
    delete_all_nodes(root)
    # delete_all_duplicates(root)
    boucle_node(root)
    test_logique(root)
    for node in PreOrderIter(root):
        if node.name != "N1":
            name = node.name.split(" ")
            if name[1] == "instruction":
                for i in range(0, len(node.children)):
                    name = node.children[i].name.split(" ")
                    if name[1] == "return":
                        return_instr(node.parent)
                    elif name[1] == "N92":
                        affect(node)
    return root


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


def boucle_node(root):
    for node in PreOrderIter(root):
        if node.name != "N1":
            rename(node)
def A2_destroyer(root):
    name = root.name.split(" ")
    root.name = name[0] + " Expr"
    for node in PreOrderIter(root):
        nameNode = node.name.split(" ")
        if nameNode[1] == "A2":
            children = node.children
            for i in range(len(children)):
                children[i].parent = node.parent
            node.parent = None


def test_logique(root):
    for node in PreOrderIter(root):
        test_if(node, "Expr")
        test_elsif(node, "Expr")
        test_else(node, "Expr")


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
                if (nameS[1] == "A2"):
                    A2_destroyer(sibling[i])
                    sibling[i].parent = node
                    break
                if(nameS[1] == "instruction"):
                    x = Node(nameS[0] + " Expr", node)
                    sibling[i].parent = x
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
                if (nameS[1] == "A2"):
                    A2_destroyer(sibling[i])
                    sibling[i].parent = node
                    break
                if(nameS[1] == "instruction"):
                    x = Node(nameS[0] + " Expr", node)
                    sibling[i].parent = x
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
                if (nameS[1] == "A2"):
                    A2_destroyer(sibling[i])
                    sibling[i].parent = node
                    break
                if (nameS[1] == "instruction"):
                    x = Node(nameS[0] + " Expr", node)
                    sibling[i].parent = x
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
