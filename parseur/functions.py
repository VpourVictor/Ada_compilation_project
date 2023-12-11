from parseur.arbre import Noeud
from lexeur.dictionnaire_ter import get_term


def fonction_N1(list_token):
    error = False
    count = 0
    # todo
    if list_token[0] == 284:  # 284 = with
        count += 1
    else:
        error = True
        print("attendu : with, reçu : " + find_receive(list_token[0]))

    if ident_ada(list_token[1]):  # 285 = Ada
        count += 1
    else:
        error = True
        print("attendu : Ada, reçu : " + find_receive(list_token[1]))

    if list_token[2] == 46:  # 46 = .
        count += 1
    else:
        error = True
        print("attendu : ., reçu : " + find_receive(list_token[2]))

    if ident_text_io(list_token[3]):  # 285 = Text_IO
        count += 1
    else:
        error = True
        print("attendu : Text_IO, reçu : " + find_receive(list_token[3]))

    if list_token[4] != 59:  # 59 = ;
        print("attendu : ;, reçu : " + find_receive(list_token[4]))

    if list_token[5] != 282: # 282 = use
        print("attendu : use, reçu : " + find_receive(list_token[5]))

    if list_token[6] != 285: # 285 = Ada
        print("attendu : Ada, reçu : " + find_receive(list_token[6]))

    if list_token[7] != 46: # 46 = .
        print("attendu : ., reçu : " + find_receive(list_token[7]))

    if list_token[8] != 285: # 285 = Text_IO
        print("attendu : Text_IO, reçu : " + find_receive(list_token[8]))

    if error:
        return [False, 8]
    else:
        return [True, 8]


def find_receive(elem):
    list_of_key = list(get_term().keys())
    list_of_value = list(get_term().values())

    if type(elem) == int:
        position = list_of_value.index(elem)
        return list_of_key[position]
    else:
        return str(elem[1])


def ident_ada(couple):
    if type(couple) != int:
        if couple[0] == 285 and couple[1] == "Ada":
            return True
    else:
        return False


def ident_text_io(couple):
    if couple[0] == 285 and couple[1] == "Text_IO":
        return True
    else:
        return False
