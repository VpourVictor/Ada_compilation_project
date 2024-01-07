from parseur.reader_carac import reader_carac


def switch_fonction(name, token_list, count_tmp):
    result = None
    match name:
        case 'A1':
            result = fonction_A1(token_list, count_tmp)

        case '.':
            result = False, count_tmp

    return result


def rec(list_att, token_list, count_tmp, count, local):
    if count_tmp == token_list.__len__():
        print("c'est fini")
        return True, count_tmp

    if type(list_att[count_tmp]) == int:
        result = reader_carac(list_att[count_tmp], token_list, count_tmp)  # with
        if result[0]:  # with
            count_tmp = result[1]
            return rec(list_att, token_list, count_tmp, count, local + 1)
    else:
        result = switch_fonction(list_att[count_tmp], token_list, count_tmp)
        if result[0]:
            count = result[1]
            count_tmp = count
            return rec(list_att, token_list, count_tmp, count, local + 1)

    return False, count


def fonction_N1(token_list):  # N1 ::= 284 285 46 285 59 282 285 46 285 59 274 285 267 A1 258 A2 261 A3 59
    count = 0
    count_tmp = count
    return rec([284, 285, 46, 285, 59, 282, 285, 46, 285, 59, 274, 285, 267, 'A1', 258, 'A2', 261, 'A3', 59],
               token_list, count_tmp, count, 0)


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
        return False, count

    # cas où c'est espilon donc forcément vrai
    return True, count


def fonction_A2(token_list, count):  # A2 ::= N9 A22
    count_tmp = count
    result = rec(['N9', 'A22'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    return False, count


def fonction_A22(token_list, count):  # A22 ::= A2 / ''
    count_tmp = count
    result = fonction_A2(token_list, count_tmp)
    if result[0]:  # A2
        count = result[1]
        return True, count

    # cas où c'est espilon donc forcément vrai
    return True, count


def fonction_A3(token_list, count):  # A3 ::= '' / A3 ::= 285
    count_tmp = count
    result = reader_carac(285, token_list, count_tmp)
    if result[0]:  # 285
        count = result[1]
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
    result = rec([281, 285, 'N21'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # N2 ::= A5 58 N4 A6 59
    count_tmp = count
    result = rec(['A5', 58, 'N4', 'A6', 59], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # N2 ::= 274 285 A7 267 A1 258 A2 261 A3 59
    count_tmp = count
    result = rec([274, 285, 'A7', 267, 'A1', 258, 'A2', 261, 'A3', 59], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # N2 ::= 264 285 A7 277 N4 267 A1 258 A2 261 A3 59
    count_tmp = count
    result = rec([264, 285, 'A7', 277, 'N4', 267, 'A1', 258, 'A2', 261, 'A3', 59], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    return False, count


def fonction_N21(token_list, count): # N21 ::= 59 / N21 ::= 267 N22
    # N21 ::= 59
    count_tmp = count
    result = reader_carac(59, token_list, count_tmp)  # ;
    if result[0]:
        count = result[0]
        return True, count

    # N21 ::= 267 N22
    count_tmp = count
    result = rec([267, 'N22'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count


def fonction_N22(token_list, count): # N22 ::= 256 285 59 / N22 ::= 275 A4 261 275 59
    # N22 ::= 256 285 59
    count_tmp = count
    result = rec([256, 285, 59], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # N22 ::= 275 A4 261 275 59
    count_tmp = count
    result = rec([275, 'A4', 261, 275, 59], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    return False, count


def fonction_A4(token_list, count):  # A4 ::= N3 A42
    count_tmp = count
    result = rec(['N3', 'A42'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    return False, count


def fonction_A42(token_list, count):  # A42 ::= A4 / ''
    count_tmp = count
    result = fonction_A4(token_list, count_tmp)
    if result[0]:  # A4
        count = result[1]
        return True, count

    # cas où c'est espilon donc forcément vrai
    return True, count


def fonction_A5(token_list, count):  # A5 ::= 285 A52
    count_tmp = count
    result = rec([285, 'A52'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    return False, count


def fonction_A52(token_list, count):  # A52 ::= '' / A52 ::= 44 A5
    count_tmp = count
    result = reader_carac(44, token_list, count_tmp)  # ,
    if result[0]:  # ,
        count_tmp = result[1]
        result = fonction_A5(token_list, count_tmp)
        if result[0]:  # A5
            count = result[1]
            return True, count

        # si on a lu, et que l'on se rend compte qu'il ne fallait pas
        return False, count

    # cas où c'est espilon donc forcément vrai
    return True, count


def fonction_A6(token_list, count):  # A6 ::= '' / A6 ::= 58 61 N8
    count_tmp = count
    result = reader_carac(58, token_list, count_tmp)  # :
    if result[0]:  # :
        count_tmp = result[1]
        result = reader_carac(61, token_list, count_tmp)  # =
        if result[0]:  # =
            count_tmp = result[1]
            result = fonction_N8(token_list, count_tmp)
            if result[0]:  # N8
                count = result[1]
                return True, count

            # si on a lu :, = et que l'on se rend compte qu'il ne fallait pas
            return False, count

        # si on a lu : et que l'on se rend compte qu'il ne fallait pas
        return False, count

    # cas où c'est espilon donc forcément vrai
    return True, count


def fonction_A7(token_list, count):  # A7 ::= '' / A7 ::= N5
    count_tmp = count
    result = fonction_N5(token_list, count_tmp)
    if result[0]:  # N5
        count = result[1]
        return True, count

    # cas où c'est espilon donc forcément vrai
    return True, count


def fonction_N3(token_list, count):  # N3 ::= A5 58 N4 59
    count_tmp = count
    result = rec(['A5', 58, 'N4', 59], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    return False, count


def fonction_N4(token_list, count):  # N4 ::= 285 / N4 ::= 256 285
    count_tmp = count
    result = reader_carac(285, token_list, count_tmp)
    if result[0]:  # 285
        count = result[1]
        return True, count

    count_tmp = count
    result = rec([256, 285], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    return False, count


def fonction_N5(token_list, count):  # N5 ::= 40 A8 41
    count_tmp = count
    result = rec([40, 'A8', 41], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    return False, count


def fonction_A8(token_list, count):  # A8 ::= N6 A82
    count_tmp = count
    result = rec(['N6', 'A82'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    return False, count


def fonction_A82(token_list, count):  # A82 ::= '' / A82 ::= 59 A8
    count_tmp = count
    result = reader_carac(59, token_list, count_tmp)  # ;
    if result[0]:  # ;
        count_tmp = result[1]
        result = fonction_A8(token_list, count_tmp)
        if result[0]:  # A8
            count = result[1]
            return True, count

        # si on a lu ; et que l'on se rend compte qu'il ne fallait pas
        return False, count

    # cas où c'est espilon donc forcément vrai
    return True, count


def fonction_N6(token_list, count):  # N6 ::= A5 58 A9 N4
    count_tmp = count
    result = rec(['A5', 58, 'A9', 'N4'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    return False, count


def fonction_A9(token_list, count):  # A9 ::= '' / A9 ::= N7
    count_tmp = count
    result = fonction_N7(token_list, count_tmp)
    if result[0]:  # N7
        count = result[1]
        return True, count

    # cas où c'est espilon donc forcément vrai
    return True, count


def fonction_N7(token_list, count):  # N7 ::= 266 N71
    count_tmp = count
    result = rec([266, 'N71'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    return False, count


def fonction_N71(token_list, count):  # N71 ::= '' / N71 ::= 273
    count_tmp = count
    result = reader_carac(273, token_list, count_tmp)  # in
    if result[0]:  # in
        count = result[1]
        return True, count

    # cas où c'est espilon donc forcément vrai
    return True, count


def fonction_N8(token_list, count):
    # N8 ::= N15
    # N8 ::= N16
    # N8 ::= 280
    # N8 ::= 262
    # N8 ::= 271
    # N8 ::= 40 N8 41
    # N8 ::= 269 285
    # N8 ::= 285 40 A10 41
    # N8 ::= 287 34 288 40 N8 41
    # N8 ::= EXPR1 EXPRA

    # N8 ::= N15
    count_tmp = count
    result = fonction_N15(token_list, count_tmp)
    if result[0]:  # N15
        count = result[1]
        return True, count

    # N8 ::= N16
    count_tmp = count
    result = fonction_N16(token_list, count_tmp)
    if result[0]:  # N16
        count = result[1]
        return True, count

    # N8 ::= 280
    count_tmp = count
    result = reader_carac(280, token_list, count_tmp)  # not
    if result[0]:  # not
        count = result[1]
        return True, count

    # N8 ::= 262
    count_tmp = count
    result = reader_carac(262, token_list, count_tmp)  # true
    if result[0]:  # true
        count = result[1]
        return True, count

    # N8 ::= 271
    count_tmp = count
    result = reader_carac(271, token_list, count_tmp)  # false
    if result[0]:  # false
        count = result[1]
        return True, count

    # N8 ::= 40 N8 41
    count_tmp = count
    result = rec([40, 'N8', 41], token_list, count_tmp, count, 0)
    if result[0]:  # ( N8 )
        count = result[1]
        return True, count

    # N8 ::= 269 285
    count_tmp = count
    result = rec([269, 285], token_list, count_tmp, count, 0)
    if result[0]:  # null
        count = result[1]
        return True, count

    # N8 ::= 285 40 A10 41
    count_tmp = count
    result = rec([285, 40, 'A10', 41], token_list, count_tmp, count, 0)
    if result[0]:  # ( A10 )
        count = result[1]
        return True, count

    # N8 ::= 287 34 288 40 N8 41
    count_tmp = count
    result = rec([287, 34, 288, 40, 'N8', 41], token_list, count_tmp, count, 0)
    if result[0]:  # ' N8 '
        count = result[1]
        return True, count

    # N8 ::= EXPR1 EXPRA
    count_tmp = count
    result = rec(['EXPR1', 'EXPRA'], token_list, count_tmp, count, 0)
    if result[0]:  # ' N8 '
        count = result[1]
        return True, count

    return False, count


def fonction_EXPRA(token_list, count): # EXPRA ::= 272 EXPRA1 / # EXPRA ::= ''

    # EXPRA ::= 272 EXPRA1
    count_tmp = count
    result = rec([272, 'EXPRA1'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # si c'est epsilon, c'est forcément vrai
    return True, count


def fonction_EXPRA1(token_list, count): # EXPRA1 ::= N8 / EXPRA1 ::= 259 N8
    # EXPRA1 ::= N8
    count_tmp = count
    result = fonction_N8(token_list, count_tmp)
    if result[0]:  # N8
        count = result[1]
        return True, count

    # EXPRA1 ::= 259 N8
    count_tmp = count
    result = rec([259, 'N8'], token_list, count_tmp, count, 0)
    if result[0]:  # N8
        count = result[1]
        return True, count

    return False, count


def fonction_EXRPR1(token_list, count): # EXPR1 ::= EXPR2 EXPRB
    count_tmp = count
    result = rec(['EXPR2', 'EXPRB'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    return False, count


def fonction_EXPRB1(token_list, count): # EXPRB1 ::= EXPR1 / EXPRB1 ::= 279 EXPR1
    # EXPRB1 ::= EXPR1
    count_tmp = count
    result = fonction_EXRPR1(token_list, count_tmp)
    if result[0]:  # EXPR1
        count = result[1]
        return True, count

    # EXPRB1 ::= 279 EXPR1
    count_tmp = count
    result = rec([279, 'EXPR1'], token_list, count_tmp, count, 0)
    if result[0]:  # EXPR1
        count = result[1]
        return True, count

    return False, count


def fonction_EXPRB(token_list, count): # EXPRB ::= 257 EXPRB1 / EXPRB ::= ''
    # EXPRB ::= 257 EXPRB1
    count_tmp = count
    result = rec([257, 'EXPRB1'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # si c'est epsilon, c'est forcément vrai
    return True, count


def fonction_EXPR2(token_list, count): # EXPR2 ::= EXPR3 / EXPR2 ::= 270 EXPR3
    # EXPR2 ::= EXPR3
    count_tmp = count
    result = fonction_EXPR3(token_list, count_tmp)
    if result[0]:  # EXPR3
        count = result[1]
        return True, count

    # EXPR2 ::= 270 EXPR3
    count_tmp = count
    result = rec([270, 'EXPR3'], token_list, count_tmp, count, 0)
    if result[0]:  # EXPR3
        count = result[1]
        return True, count

    return False, count


def fonction_EXPR3(token_list, count): # EXPR3 ::= EXPR4 EXPRC
    count_tmp = count
    result = rec(['EXPR4', 'EXPRC'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    return False, count


def fonction_EXPRC(token_list, count):
    # EXPRC ::= 61 EXPR4 EXPRC
    # EXPRC ::= 47 61 EXPR4 EXPRC
    # EXPRC ::= ''

    # EXPRC ::= 61 EXPR4 EXPRC
    count_tmp = count
    result = rec([61, 'EXPR4', 'EXPRC'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # EXPRC ::= 47 61 EXPR4 EXPRC
    count_tmp = count
    result = rec([47, 61, 'EXPR4', 'EXPRC'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # si c'est epsilon, c'est forcément vrai
    return True, count


def fonction_EXPR4(token_list, count): # EXPR4 ::= EXPR5 EXPRE
    count_tmp = count
    result = rec(['EXPR5', 'EXPRE'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    return False, count


def fonction_EXPRE(token_list, count):
    # EXPRE ::= 60 EXPRE1
    # EXPRE ::= 62 EXPRE2
    # EXPRE ::= ''

    # EXPRE ::= 60 EXPRE1
    count_tmp = count
    result = rec([60, 'EXPRE1'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # EXPRE ::= 62 EXPRE2
    count_tmp = count
    result = rec([62, 'EXPRE2'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # si c'est epsilon, c'est forcément vrai
    return True, count


def fonction_EXPRE1(token_list, count): # EXPRE1 ::= EXPR5 EXPRE / EXPRE1 ::= 61 EXPR5 EXPRE
    # EXPRE1 ::= EXPR5 EXPRE
    count_tmp = count
    result = rec(['EXPR5', 'EXPRE'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # EXPRE1 ::= 61 EXPR5 EXPRE
    count_tmp = count
    result = rec([61, 'EXPR5', 'EXPRE'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    return False, count


# todo !!!!! problème pas LL1
def fonction_EXPRE2(token_list, count): # EXPRE2 ::= EXPR5 EXPRE / EXPRE2 ::= 61 EXPR5 EXPRE
    # EXPRE2 ::= EXPR5 EXPRE
    count_tmp = count
    result = rec(['EXPR5', 'EXPRE'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # EXPRE2 ::= 61 EXPR5 EXPRE
    count_tmp = count
    result = rec([61, 'EXPR5', 'EXPRE'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    return False, count


def fonction_EXPR5(token_list, count): # EXPR5 ::= EXPR6 EXPRF
    count_tmp = count
    result = rec(['EXPR6', 'EXPRF'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    return False, count


def fonction_EXPRF(token_list, count):
    # EXPRF ::= 43 EXPR6 EXPRF
    # EXPRF ::= 45 EXPR6 EXPRF
    # EXPRF ::= ''

    # EXPRF ::= 43 EXPR6 EXPRF
    count_tmp = count
    result = rec([43, 'EXPR6', 'EXPRF'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # EXPRF ::= 45 EXPR6 EXPRF
    count_tmp = count
    result = rec([45, 'EXPR6', 'EXPRF'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # si c'est epsilon, c'est forcément vrai
    return True, count


def fonction_EXPR6(token_list, count): # EXPR6 ::= EXPR7 EXPRG
    count_tmp = count
    result = rec(['EXPR7', 'EXPRG'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    return False, count


def fonction_EXPRG(token_list, count):
    # EXPRG ::= 42 EXPR7 EXPRG
    # EXPRG ::= 47 EXPR7 EXPRG
    # EXPRG ::= 276 EXPR7 EXPRG
    # EXPRG ::= ''

    # EXPRG ::= 42 EXPR7 EXPRG
    count_tmp = count
    result = rec([42, 'EXPR7', 'EXPRG'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # EXPRG ::= 47 EXPR7 EXPRG
    count_tmp = count
    result = rec([47, 'EXPR7', 'EXPRG'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # EXPRG ::= 276 EXPR7 EXPRG
    count_tmp = count
    result = rec([276, 'EXPR7', 'EXPRG'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # si c'est epsilon, c'est forcément vrai
    return True, count


def fonction_EXPR7(token_list, count):
    # EXPR7 ::= EXPR8
    # EXPR7 ::= 45 EXPR8

    # EXPR7 ::= EXPR8
    count_tmp = count
    result = fonction_EXPR8(token_list, count_tmp)
    if result[0]:  # EXPR8
        count = result[1]
        return True, count

    # EXPR7 ::= 45 EXPR8
    count_tmp = count
    result = rec([45, 'EXPR8'], token_list, count_tmp, count, 0)
    if result[0]:  # EXPR8
        count = result[1]
        return True, count

    return False, count


# todo !!!!! Voir à quoi correspond ACCES
def fonction_EXPR8(token_list, count):
    # EXPR8 ::= ACCES
