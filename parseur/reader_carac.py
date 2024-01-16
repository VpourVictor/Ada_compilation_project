from parseur.compare import compare


def reader_carac(val, token_list, count_tmp):
    # on différencie les cas où on a un int ou un tuple
    if not (type(token_list[count_tmp]) == int): # (tuple)
        var, chaine = token_list[count_tmp]
        # on compare la valeur du token (la clé du tuple), avec la valeur attendue (num dans la règle > val)
        if var == val:
            # si cela convient, on avance dans la liste de token
            count_tmp += 1
            # on renvoie True et le nouveau compteur
            return True, count_tmp
        else:
            # sinon, on renvoie une erreur sans avoir modifié le compteur
            return False, count_tmp
    # cas où on a un int (donc un token)
    # on procède à la comparaison
    elif val == token_list[count_tmp]:
        # si cela convient, on avance dans la liste de token
        count_tmp += 1
        return True, count_tmp
    else:
        # sinon, on renvoie une erreur sans avoir modifié le compteur
        return False, count_tmp
