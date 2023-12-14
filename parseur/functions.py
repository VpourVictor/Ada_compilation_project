from parseur.reader_carac import reader_carac


def switch_fonction(name, token_list, count_tmp):
    result = None
    match name:
        case 'A1':
            result = fonction_A1(token_list, count_tmp)

        case '.':
            result = False, count_tmp

    return result


def rec(list_att, token_list, count_tmp, count):
    if type(list_att[count_tmp]) == int:
        result = reader_carac(list_att[count_tmp], token_list, count_tmp)  # with
        if result[0]:  # with
            count_tmp = result[1]
            return rec(list_att, token_list, count_tmp, count)
    else:
        result = switch_fonction(list_att[count_tmp], token_list, count_tmp)
        if result[0]:
            count = result[1]
            count_tmp = count
            return rec(list_att, token_list, count_tmp, count)

    # voir si c'est vraiment bien ca la fin (true ou false)
    return False, count


def fonction_N1(token_list):  # N1 ::= 284 285 46 285 59 282 285 46 285 59 274 285 267 A1 258 A2 261 A3 59
    count = 0
    count_tmp = count
    return rec([284, 285, 46, 285, 59, 282, 285, 46, 285, 59, 274, 285, 267, 'A1', 258, 'A2', 261, 'A3', 59], token_list,
        count_tmp, count)


def fonction_A1(token_list, count):  # A1 ::= '' / A1 ::= N2 A1
    count_tmp = count
    result = fonction_N2(token_list, count_tmp)
    if result[0]:  # N2
        # on ne change pas tout de suite le count
        # car si on se rend compte qu'il ne fallait pas lire N2, on n'est pas bloqué
        count_tmp = result[1]
        result = fonction_A1(token_list, count_tmp)
        if result[0]:  # A1
            count = result[1]
            return True, count

        # si on a lu N2 et que l'on se rend compte qu'il ne fallait pas
        return True, count

    # cas où c'est espilon donc forcément vrai
    return True, count


def fonction_N2(token_list, count):
    # N2 ::= 281 285 N21
    # N2 ::= A5 58 N4 A6 59
    # N2 ::= 274 285 A7 267 A1 258 A2 261 A3 59
    # N2 ::= 264 285 A7 277 N4 267 A1 258 A2 261 A3 59

    # N2 ::= 281 285 N21
    count_tmp = count
    rec([281, 285, 'N21'], token_list, count_tmp, count)

    # N2 ::= A5 58 N4 A6 59
    count_tmp = count
    rec(['A5', 58, 'N4', 'A6', 59], token_list, count_tmp, count)

    # N2 ::= 274 285 A7 267 A1 258 A2 261 A3 59
    count_tmp = count
    result = reader_carac(274, token_list, count_tmp)  # procedure
    if result[0]:
        count_tmp = result[1]
        result = reader_carac(285, token_list, count_tmp)  # id
        if result[0]:
            count_tmp = result[1]
            result = fonction_A7(token_list, count_tmp)
            if result[0]:
                count = result[1]
                count_tmp = count
                result = reader_carac(267, token_list, count_tmp)  # is
                if result[0]:
                    count_tmp = result[1]
                    result = fonction_A1(token_list, count_tmp)
                    if result[0]:
                        count = result[1]
                        count_tmp = count
                        result = reader_carac(258, token_list, count_tmp)  # begin
                        if result[0]:
                            count_tmp = result[1]
                            result = fonction_A2(token_list, count_tmp)
                            if result[0]:
                                count = result[1]
                                count_tmp = count
                                result = reader_carac(261, token_list, count_tmp)  # end
                                if result[0]:
                                    count_tmp = result[1]
                                    result = fonction_A3(token_list, count_tmp)
                                    if result[0]:
                                        count = result[1]
                                        count_tmp = count
                                        result = reader_carac(59, token_list, count_tmp)  # ;
                                        if result[0]:
                                            count = result[1]
                                            return True, count

    # N2 ::= 264 285 A7 277 N4 267 A1 258 A2 261 A3 59
    count_tmp = count
    result = reader_carac(264, token_list, count_tmp)  # function
    if result[0]:
        count_tmp = result[1]
        result = reader_carac(285, token_list, count_tmp)  # id
        if result[0]:
            count_tmp = result[1]
            result = fonction_A7(token_list, count_tmp)
            if result[0]:
                count = result[1]
                count_tmp = count
                result = reader_carac(277, token_list, count_tmp)  # return
                if result[0]:
                    count_tmp = result[1]
                    result = fonction_N4(token_list, count_tmp)
                    if result[0]:
                        count = result[1]
                        count_tmp = count
                        result = reader_carac(267, token_list, count_tmp)  # is
                        if result[0]:
                            count_tmp = result[1]
                            result = fonction_A1(token_list, count_tmp)
                            if result[0]:
                                count = result[1]
                                count_tmp = count
                                result = reader_carac(258, token_list, count_tmp)  # begin
                                if result[0]:
                                    count_tmp = result[1]
                                    result = fonction_A2(token_list, count_tmp)
                                    if result[0]:
                                        count = result[1]
                                        count_tmp = count
                                        result = reader_carac(261, token_list, count_tmp)  # end
                                        if result[0]:
                                            count_tmp = result[1]
                                            result = fonction_A3(token_list, count_tmp)
                                            if result[0]:
                                                count = result[1]
                                                count_tmp = count
                                                result = reader_carac(59, token_list, count_tmp)  # ;
                                                if result[0]:
                                                    count = result[1]
                                                    return True, count
    return False, count


def fonction_N21(token_list, count):  # N21 ::= 59 / N21 ::= 267 N22
    count_tmp = count
    result = reader_carac(59, token_list, count_tmp)  # ;
    if result[0]:
        count = result[0]
        return True, count

    count = count_tmp
    result = reader_carac(267, token_list, count_tmp)  # is
    if result[0]:
        count_tmp = result[1]
        result = fonction_N22(token_list, count_tmp)
        if result[0]:
            count = result[1]
            return True, count

    return False, count
