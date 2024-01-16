from anytree import Node, RenderTree, search, PreOrderIter
from anytree.exporter import DotExporter

import lexeur.file_to_code_ter as file
import parseur.functions


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
    delete_leef_epsX(root)
    generate_tree("tree_calcul.png")
    result = search.findall(root, filter_=lambda node: node.name in ("33 285"))
    print(result)

    # print("On va maintenant tester un exemple qui contient des procédures imbriquées :")
    # token_list = file.get_token("exemples/exemple_double_procedure.ada")
    # print(token_list)
    # root = Node('N1')
    # print(parseur.functions.fonction_N1(token_list, root))
    # delete_leef_epsX(root)
    # generate_tree("tree_double_procedure.png")
    #
    # print("On va maintenant tester un exemple qui contient blocs d'instructions if elif et else :")
    # token_list = file.get_token("exemples/exemple_if_elif.ada")
    # print(token_list)
    # root = Node('N1')
    # print(parseur.functions.fonction_N1(token_list, root))
    # delete_leef_epsX(root)
    # generate_tree("tree_if_elif.png")
    #
    # print("On va maintenant tester si notre parseur fonctionne avec un programme qui contient des if et des while :")
    # token_list = file.get_token("exemples/exemple_if_while.ada")
    # print(token_list)
    # root = Node('N1')
    # print(parseur.functions.fonction_N1(token_list, root))
    # delete_leef_epsX(root)
    # generate_tree("tree_if_while.png")
    #
    # print("Le test qui suit vise à montrer que l'on traite bien le cas où notre grammaire n'est pas LL1 (/=, /) :")
    # token_list = file.get_token("exemples/exemple_division_difference.ada")
    # print(token_list)
    # root = Node('N1')
    # print(parseur.functions.fonction_N1(token_list, root))
    # delete_leef_epsX(root)
    # generate_tree("tree_division_difference.png")
    #
    # print("On va maintenant tester un exemple qui tourne autour des expressions arithmétiques :")
    # token_list = file.get_token("exemples/exemple_expression_arithmetique.ada")
    # print(token_list)
    # root = Node('N1')
    # print(parseur.functions.fonction_N1(token_list, root))
    # delete_leef_epsX(root)
    # generate_tree("tree_expression_arithmetique.png")
    #
    # print("On va maintenant tester un exemple qui contient des fonctions imbriquées :")
    # token_list = file.get_token("exemples/exemple_fonctions_imb.ada")
    # print(token_list)
    # root = Node('N1')
    # print(parseur.functions.fonction_N1(token_list, root))
    # delete_leef_epsX(root)
    # generate_tree("tree_fonctions_imb.png")
    #
    # print("On va maintenant tester un exemple qui mélange un peut tout (fonctions, procédures) :")
    # token_list = file.get_token("exemples/exemple_mixte.ada")
    # print(token_list)
    # root = Node('N1')
    # print(parseur.functions.fonction_N1(token_list, root))
    # delete_leef_epsX(root)
    # generate_tree("tree_mixte.png")
    #
    # print("Le dernier test est effectué sur le code fournit dans le sujet :")
    # token_list = file.get_token("exemples/exemple.ada")
    # print(token_list)
    # root = Node('N1')
    # print(parseur.functions.fonction_N1(token_list, root))
    # delete_leef_epsX(root)
    # generate_tree("tree_exemple.png")

    # Display the tree structure
    # for pre, _, node in RenderTree(root):
    #     print(f"{pre}{node.name}")
