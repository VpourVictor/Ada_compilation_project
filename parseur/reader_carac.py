from parseur.compare import compare


def reader_carac(val, token_list, count_tmp):
    if compare(val, token_list[count_tmp]):
        # si cela convient, on avance dans la liste de token
        count_tmp += 1
        return True, count_tmp
        # sinon, on renvoie une erreur sans avoir modifié le compteur
    else:
        return False, count_tmp
            


