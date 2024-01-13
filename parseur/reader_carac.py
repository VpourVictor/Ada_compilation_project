from parseur.compare import compare


def reader_carac(val, token_list, count_tmp):
    # if count_tmp >= len(token_list):
        # return False, count_tmp
    # tuple ou pas
    # si c'est un couple ou int et que c'est ce qu'on cherche, ok
    # si ce n'est pas le cas, on passe dans compare
    if not (type(token_list[count_tmp]) == int): # (tuple)
        var, chaine = token_list[count_tmp]
        if var == val:
            count_tmp += 1
            return True, count_tmp
        else:
            return False, count_tmp
    elif val == token_list[count_tmp]:  # si bonne valeur (int)
        count_tmp += 1
        return True, count_tmp
    else:
        return False, count_tmp
