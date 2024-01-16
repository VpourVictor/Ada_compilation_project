from anytree import Node, RenderTree, search, PreOrderIter
from anytree.exporter import DotExporter

import lexeur.file_to_code_ter as file
import parseur.functions

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
    return nom[1][0].isalpha()


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
        while j != l - 1:
            if children[j+nb_of_del].name in (L[:j] + L[j + 1:]):
                nb_of_del += 1
                children[j+nb_of_del].parent = None
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


def delete_all_nodes(root):
    for node in PreOrderIter(root):
        if supprimer_noeuds_un_seul_fils(node):
            delete_all_nodes(root)


def generate_final_AST(root):
    delete_leef_epsX(root)
    delete_all_nodes(root)
    # delete_all_duplicates(root)
    return root


def countleaves(node):
    return sum(1 for _ in PreOrderIter(node, filter_=lambda x: x.is_leaf))


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
