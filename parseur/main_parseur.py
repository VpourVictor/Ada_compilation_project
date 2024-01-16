import filecmp

import 


def generate_tree(name_file):
    try:
        DotExporter(root).to_picture(filename=name_file)
        print("Tree visualization saved")
    except ImportError:
        print("Graphviz not installed. Unable to create graphical representation.")


if __name__ == '__main__':
    # print("On va maintenant tester notre parseur")
    # print("Pour chaque test, on va afficher la liste de token renvoyé par le lexeur, puis générer l'arbre syntaxique "
    #       "associé")
    # print("On va tester les exemples suivants :")
    # print("On commence par un exemple simple : un programme qui se charge de faire une somme entre 2 entiers :")
    # token_list = file.get_token("exemples/exemple_calcul.ada")
    # print(token_list)
    # root = Node('N1')
    # print(parseur.functions.fonction_N1(token_list, root))
    # generate_tree("tree_calcul.png")
    #
    # print("On va maintenant tester un exemple qui contient des procédures imbriquées :")
    # token_list = file.get_token("exemples/exemple_double_procedure.ada")
    # print(token_list)
    # root = Node('N1')
    # print(parseur.functions.fonction_N1(token_list, root))
    # generate_tree("tree_double_procedure.png")
    #
    # print("On va maintenant tester un exemple qui contient blocs d'instructions if elif et else :")
    # token_list = file.get_token("exemples/exemple_if_elif.ada")
    # print(token_list)
    # root = Node('N1)
    # print(parseur.functions.fonction_N1(token_list, root))
    # generate_tree("tree_if_elif.png")

    # todo ne marche pas
    print("On va maintenant tester si notre parseur fonctionne avec un programme qui contient des if et des while :")
    token_list = filecmp.get_token("exemples/exemple_if_while.ada")
    print(token_list)
    root = Node('N1')
    print(parseur.functions.fonction_N1(token_list, root))
    generate_tree("tree_if_while.png")

    # todo ne marche pas
    # print("Le test qui suit vise à montrer que l'on traite bien le cas où notre grammaire n'est pas LL1 (/=, /) :")
    # token_list = file.get_token("exemples/exemple_division_difference.ada")
    # print(token_list)
    # root = Node('N1')
    # print(parseur.functions.fonction_N1(token_list, root))
    # generate_tree("tree_division_difference.png")

    # todo ne marche pas
    # print("On va maintenant tester un exemple qui contient des fonctions imbriquées :")
    # token_list = file.get_token("exemples/exemple_fonctions_imb.ada")
    # print(token_list)
    # root = Node('N1')
    # print(parseur.functions.fonction_N1(token_list, root))
    # generate_tree("tree_fonctions_imb.png")

    # todo ne marche pas
    # print("On va maintenant tester un exemple qui mélange un peut tout (fonctions, procédures) :")
    # token_list = file.get_token("exemples/exemple_mixte.ada")
    # print(token_list)
    # root = Node('N1')
    # print(parseur.functions.fonction_N1(token_list, root))
    # generate_tree("tree_mixte.png")

    # todo ne marche pas
    # print("Le dernier test est effectué sur le code fournit dans le sujet :")
    # token_list = file.get_token("exemples/exemple.ada")
    # print(token_list)
    # root = Node('N1')
    # print(parseur.functions.fonction_N1(token_list, root))
    # generate_tree("tree_exemple.png")

    # Display the tree structure
    # for pre, _, node in RenderTree(root):
    #     print(f"{pre}{node.name}")
