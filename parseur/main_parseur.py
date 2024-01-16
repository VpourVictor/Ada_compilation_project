from anytree import Node, RenderTree

import lexeur.file_to_code_ter as file
import parseur.functions
import lexeur.dictionnaire_ter as dictionnaire_ter

if __name__ == '__main__':
    # token_list = file.get_token("exemples/intro.ada")
    # print(token_list)
    # print(parseur.functions.fonction_N1(token_list))
    print(dictionnaire_ter.term)
    root = Node('N1')

    token_list = file.get_token("exemples/exemple_calcul.ada") # -> fonctionne
    # token_list = file.get_token("exemples/exemple_petite_procedure.ada") # -> fonctionne

    # token_list = file.get_token("exemples/exemple_if.ada")
    # token_list = file.get_token("exemples/exemple_procedure.ada")
    # token_list = file.get_token("exemples/exemple.ada")
    # token_list = file.get_token("exemples/exemple_fonctions_imb.ada")
    print(token_list)
    print(parseur.functions.fonction_N1(token_list, root))
    # Display the tree structure
    for pre, _, node in RenderTree(root):
        print(f"{pre}{node.name}")

    try:
        from anytree.exporter import DotExporter

        DotExporter(root).to_picture("tree.png")
        print("Tree visualization saved as tree.png")
    except ImportError:
        print("Graphviz not installed. Unable to create graphical representation.")
