from parseur.compare import compare


def reader_carac(val, token_list, count_tmp, count):
    # tuple ou pas
    # si c'est un couple, on check si c'est la chaine qu'on attend
    # si ce n'est pas le cas, on passe dans compare

    # si c'est un int, on test si c'est la valeur qu'on attend
    # si ou, on renvoie True, sinon false

    if val == token_list[count_tmp]:  # si bonne valeur
        count_tmp += 1
        return True, count_tmp
    elif compare(val, token_list[count_tmp], count_tmp, count):
        count_tmp += 1
        return True, count_tmp
    else:
        return False, count_tmp
