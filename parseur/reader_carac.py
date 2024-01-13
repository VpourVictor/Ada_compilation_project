from parseur.compare import compare


def reader_carac(val, token_list, count_tmp, count):
    # tuple ou pas
    if val == token_list[count_tmp]:  # si bonne valeur
        count_tmp += 1
        return True, count_tmp
    elif compare(val, token_list[count_tmp], count_tmp, count):
        count_tmp += 1
        return True, count_tmp
    else:
        return False, count_tmp
            


