from parseur.reader_carac import reader_carac


def switch_fonction(name, token_list, count_tmp):
    result = None
    match name:
        case 'A1':
            print("---------------------------------------------------------------------> entrée A1")
            result = fonction_A1(token_list, count_tmp)
        case 'A2':
            print("---------------------------------------------------------------------> entrée A2")
            result = fonction_A2(token_list, count_tmp)
        case 'A22':
            result = fonction_A22(token_list, count_tmp)
        case 'A3':
            print("---------------------------------------------------------------------> entrée A3")
            result = fonction_A3(token_list, count_tmp)
        case 'A4':
            print("---------------------------------------------------------------------> entrée A4")
            result = fonction_A4(token_list, count_tmp)
        case 'A42':
            print("---------------------------------------------------------------------> entrée A42")
            result = fonction_A42(token_list, count_tmp)
        case 'A5':
            print("---------------------------------------------------------------------> entrée A5")
            result = fonction_A5(token_list, count_tmp)
        case 'A52':
            print("---------------------------------------------------------------------> entrée A52")
            result = fonction_A52(token_list, count_tmp)
        case 'A6':
            print("---------------------------------------------------------------------> entrée A6")
            result = fonction_A6(token_list, count_tmp)
        case 'A7':
            print("---------------------------------------------------------------------> entrée A7")
            result = fonction_A7(token_list, count_tmp)
        case 'A8':
            print("---------------------------------------------------------------------> entrée A8")
            result = fonction_A8(token_list, count_tmp)
        case 'A82':
            print("---------------------------------------------------------------------> entrée A82")
            result = fonction_A82(token_list, count_tmp)
        case 'A9':
            print("---------------------------------------------------------------------> entrée A9")
            result = fonction_A9(token_list, count_tmp)
        case 'A10':
            print("---------------------------------------------------------------------> entrée A10")
            result = fonction_A10(token_list, count_tmp)
        case 'A102':
            print("---------------------------------------------------------------------> entrée A102")
            result = fonction_A102(token_list, count_tmp)
        case 'A11':
            print("---------------------------------------------------------------------> entrée A11")
            result = fonction_A11(token_list, count_tmp)
        case 'A12':
            print("---------------------------------------------------------------------> entrée A12")
            result = fonction_A12(token_list, count_tmp)
        case 'A13':
            print("---------------------------------------------------------------------> entrée A13")
            result = fonction_A13(token_list, count_tmp)
        case 'A14':
            print("---------------------------------------------------------------------> entrée A14")
            result = fonction_A14(token_list, count_tmp)
        case 'A15':
            print("---------------------------------------------------------------------> entrée A15")
            result = fonction_A15(token_list, count_tmp)
        case 'A16':
            print("---------------------------------------------------------------------> entrée A16")
            result = fonction_A16(token_list, count_tmp)
        case 'N11':
            print("---------------------------------------------------------------------> entrée N11")
            result = fonction_N11(token_list, count_tmp)
        case 'N111':
            print("---------------------------------------------------------------------> entrée N111")
            result = fonction_N111(token_list, count_tmp)
        case 'N12':
            print("---------------------------------------------------------------------> entrée N12")
            result = fonction_N12(token_list, count_tmp)
        case 'N13':
            print("---------------------------------------------------------------------> entrée N13")
            result = fonction_N13(token_list, count_tmp)
        case 'N16':
            print("---------------------------------------------------------------------> entrée N16")
            result = fonction_N16(token_list, count_tmp)
        case 'N2':
            print("---------------------------------------------------------------------> entrée N2")
            result = fonction_N2(token_list, count_tmp)
        case 'N21':
            print("---------------------------------------------------------------------> entrée N21")
            result = fonction_N21(token_list, count_tmp)
        case 'N22':
            print("---------------------------------------------------------------------> entrée N22")
            result = fonction_N22(token_list, count_tmp)
        case 'N3':
            print("---------------------------------------------------------------------> entrée N3")
            result = fonction_N3(token_list, count_tmp)
        case 'N4':
            print("---------------------------------------------------------------------> entrée N4")
            result = fonction_N4(token_list, count_tmp)
        case 'N5':
            print("---------------------------------------------------------------------> entrée N5")
            result = fonction_N5(token_list, count_tmp)
        case 'N6':
            print("---------------------------------------------------------------------> entrée N6")
            result = fonction_N6(token_list, count_tmp)
        case 'N7':
            print("---------------------------------------------------------------------> entrée N7")
            result = fonction_N7(token_list, count_tmp)
        case 'N71':
            print("---------------------------------------------------------------------> entrée N71")
            result = fonction_N71(token_list, count_tmp)
        case 'N8':
            print("---------------------------------------------------------------------> entrée N8")
            result = fonction_N8(token_list, count_tmp)
        case 'N9':
            print("---------------------------------------------------------------------> entrée N9")
            result = fonction_N9(token_list, count_tmp)
        case 'N92':
            print("---------------------------------------------------------------------> entrée N92")
            result = fonction_N92(token_list, count_tmp)
        case 'N93':
            print("---------------------------------------------------------------------> entrée N93")
            result = fonction_N93(token_list, count_tmp)
        case 'N16':
            print("---------------------------------------------------------------------> entrée N16")
            result = fonction_N16(token_list, count_tmp)
        case 'EXPRA':
            print("---------------------------------------------------------------------> entrée EXPRA")
            result = fonction_EXPRA(token_list, count_tmp)
        case 'EXPRA1':
            print("---------------------------------------------------------------------> entrée EXPRA1")
            result = fonction_EXPRA1(token_list, count_tmp)
        case 'EXPR1':
            print("---------------------------------------------------------------------> entrée EXPR1")
            result = fonction_EXRPR1(token_list, count_tmp)
        case 'EXPRB1':
            print("---------------------------------------------------------------------> entrée EXPRB1")
            result = fonction_EXPRB1(token_list, count_tmp)
        case 'EXPRB':
            print("---------------------------------------------------------------------> entrée EXPRB")
            result = fonction_EXPRB(token_list, count_tmp)
        case 'EXPR2':
            print("---------------------------------------------------------------------> entrée EXPR2")
            result = fonction_EXPR2(token_list, count_tmp)
        case 'EXPR3':
            print("---------------------------------------------------------------------> entrée EXPR3")
            result = fonction_EXPR3(token_list, count_tmp)
        case 'EXPRC':
            print("---------------------------------------------------------------------> entrée EXPRC")
            result = fonction_EXPRC(token_list, count_tmp)
        case 'EXPR4':
            print("---------------------------------------------------------------------> entrée EXPR4")
            result = fonction_EXPR4(token_list, count_tmp)
        case 'EXPRE':
            print("---------------------------------------------------------------------> entrée EXPRE")
            result = fonction_EXPRE(token_list, count_tmp)
        case 'EXPRE1':
            print("---------------------------------------------------------------------> entrée EXPRE1")
            result = fonction_EXPRE1(token_list, count_tmp)
        case 'EXPRE2':
            print("---------------------------------------------------------------------> entrée EXPRE2")
            result = fonction_EXPRE2(token_list, count_tmp)
        case 'EXPR5':
            print("---------------------------------------------------------------------> entrée EXPR5")
            result = fonction_EXPR5(token_list, count_tmp)
        case 'EXPRF':
            print("---------------------------------------------------------------------> entrée EXPRF")
            result = fonction_EXPRF(token_list, count_tmp)
        case 'EXPR6':
            print("---------------------------------------------------------------------> entrée EXPR6")
            result = fonction_EXPR6(token_list, count_tmp)
        case 'EXPRG':
            print("---------------------------------------------------------------------> entrée EXPRG")
            result = fonction_EXPRG(token_list, count_tmp)
        case 'EXPR7':
            print("---------------------------------------------------------------------> entrée EXPR7")
            result = fonction_EXPR7(token_list, count_tmp)
        case 'EXPR8':
            print("---------------------------------------------------------------------> entrée EXPR8")
            result = fonction_EXPR8(token_list, count_tmp)
        case '.':
            print("---------------------------------------------------------------------> entrée .")
            result = False, count_tmp

    return result


def rec(list_att, token_list, count_tmp, count, local):
    if count_tmp == len(token_list) - 1:
        return True, count_tmp


    print("On commence le rec local avec la lecture de : " + str(list_att[local]) + " liste locale : " + str(list_att))
    if type(list_att[local]) == int:
        result = reader_carac(list_att[local], token_list, count_tmp)
        if result[0]:
            count_tmp = result[1]
            # cas où on est à la fin de la liste
            if local == len(list_att) - 1:
                print("INT : On termine le tableau local, dernier terme lu = " + str(list_att[local]) + " avec count_tmp : ", count_tmp)
                return True, count_tmp
            print("INT : On continue le local, ON RENVOIE VRAI en lisant " + str(list_att[local]) + " avec count_tmp : ", count_tmp)
            return rec(list_att, token_list, count_tmp, count, local + 1)
        else:
            print("INT : On a pas trouvé le bon caractère, ON RENVOIE FAUX avec count_tmp : ", count_tmp)
            return False, count_tmp
    else:
        result = switch_fonction(list_att[local], token_list, count_tmp)
        if result[0]:
            count = result[1]
            count_tmp = count
            # cas où on est à la fin de la liste
            if local == len(list_att) - 1:
                print("NON TERM : On termine le tableau local, dernier terme lu = " + str(list_att[local]) + " avec count_tmp : ", count_tmp)
                return True, count_tmp
            print("NON TERM : On continue le local, ON RENVOIE VRAI en lisant " + str(list_att[local]) + " avec count_tmp : ", count_tmp)
            return rec(list_att, token_list, count_tmp, count, local + 1)
        else:
            print("INT : La fonction n'est pas la bonne, ON RENVOIE FAUX avec count_tmp : ", count_tmp)
            return False, count_tmp


def fonction_N1(token_list):  # N1 ::= 284 285 46 285 59 282 285 46 285 59 274 285 267 A1 258 A2 261 A3 59
    count = 0
    count_tmp = count
    return rec([284, 285, 46, 285, 59, 282, 285, 46, 285, 59, 274, 285, 267, 'A1', 258, 'A2', 261, 'A3', 59],
               token_list, count_tmp, count, 0)


def fonction_A1(token_list, count):  # A1 ::= '' / A1 ::= N2 A1
    count_tmp = count
    result = rec(['N2'], token_list, count_tmp, count, 0)
    if result[0]:  # N2
        # on ne change pas tout de suite le count
        # car si on se rend compte qu'il ne fallait pas lire N2, on n'est pas bloqué
        count_tmp = result[1]
        result = rec(['A1'], token_list, count_tmp, count, 0)
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
    result = rec(['A2'], token_list, count_tmp, count, 0)
    if result[0]:  # A2
        count = result[1]
        return True, count

    # cas où c'est espilon donc forcément vrai
    return True, count


def fonction_A3(token_list, count):  # A3 ::= '' / A3 ::= 285
    count_tmp = count
    result = rec([285], token_list, count_tmp, count, 0)
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


def fonction_N21(token_list, count):  # N21 ::= 59 / N21 ::= 267 N22
    # N21 ::= 59
    count_tmp = count
    result = rec([59], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[0]
        return True, count

    # N21 ::= 267 N22
    count_tmp = count
    result = rec([267, 'N22'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count


def fonction_N22(token_list, count):  # N22 ::= 256 285 59 / N22 ::= 275 A4 261 275 59
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
    result = rec(['A4'], token_list, count_tmp, count, 0)
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
    result = rec([44], token_list, count_tmp, count, 0)
    if result[0]:  # ,
        count_tmp = result[1]
        result = rec(['A5'], token_list, count_tmp, count, 0)
        if result[0]:  # A5
            count = result[1]
            return True, count
        # si on a lu, et que l'on se rend compte qu'il ne fallait pas
        return False, count

    # cas où c'est espilon donc forcément vrai
    return True, count


def fonction_A6(token_list, count):  # A6 ::= '' / A6 ::= 58 61 N8
    count_tmp = count
    result = rec([58], token_list, count_tmp, count, 0)
    if result[0]:  # :
        count_tmp = result[1]
        result = rec([61], token_list, count_tmp, count, 0)
        if result[0]:  # =
            count_tmp = result[1]
            result = rec(['N8'], token_list, count_tmp, count, 0)
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
    result = rec(['N5'], token_list, count_tmp, count, 0)
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
    result = rec([285], token_list, count_tmp, count, 0)
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
    result = rec([59], token_list, count_tmp, count, 0)
    if result[0]:  # ;
        count_tmp = result[1]
        result = rec(['A8'], token_list, count_tmp, count, 0)
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
    result = rec(['N7'], token_list, count_tmp, count, 0)
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
    result = rec([273], token_list, count_tmp, count, 0)
    if result[0]:  # in
        count = result[1]
        return True, count

    # cas où c'est espilon donc forcément vrai
    return True, count


def fonction_N8(token_list, count):
    # N8 ::= 286
    # N8 ::= N16
    # N8 ::= 280
    # N8 ::= 262
    # N8 ::= 271
    # N8 ::= 40 N8 41
    # N8 ::= 269 285
    # N8 ::= 285 40 A10 41
    # N8 ::= 287 34 288 40 N8 41
    # N8 ::= EXPR1 EXPRA

    # N8 ::= 286 car chiffre
    count_tmp = count
    result = rec([286], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # N8 ::= N16
    count_tmp = count
    result = rec(['N16'], token_list, count_tmp, count, 0)
    if result[0]:  # N16
        count = result[1]
        return True, count

    # N8 ::= 280
    count_tmp = count
    result = rec([280], token_list, count_tmp, count, 0)
    if result[0]:  # not
        count = result[1]
        return True, count

    # N8 ::= 262
    count_tmp = count
    result = rec([262], token_list, count_tmp, count, 0)
    if result[0]:  # true
        count = result[1]
        return True, count

    # N8 ::= 271
    count_tmp = count
    result = rec([271], token_list, count_tmp, count, 0)
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


def fonction_EXPRA(token_list, count):  # EXPRA ::= 272 EXPRA1 / # EXPRA ::= ''

    # EXPRA ::= 272 EXPRA1
    count_tmp = count
    result = rec([272, 'EXPRA1'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # si c'est epsilon, c'est forcément vrai
    return True, count


def fonction_EXPRA1(token_list, count):  # EXPRA1 ::= N8 / EXPRA1 ::= 259 N8
    # EXPRA1 ::= N8
    count_tmp = count
    result = rec(['N8'], token_list, count_tmp, count, 0)
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


def fonction_EXRPR1(token_list, count):  # EXPR1 ::= EXPR2 EXPRB
    count_tmp = count
    result = rec(['EXPR2', 'EXPRB'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    return False, count


def fonction_EXPRB1(token_list, count):  # EXPRB1 ::= EXPR1 / EXPRB1 ::= 279 EXPR1
    # EXPRB1 ::= EXPR1
    count_tmp = count
    result = rec(['EXPR1'], token_list, count_tmp, count, 0)
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


def fonction_EXPRB(token_list, count):  # EXPRB ::= 257 EXPRB1 / EXPRB ::= ''
    # EXPRB ::= 257 EXPRB1
    count_tmp = count
    result = rec([257, 'EXPRB1'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # si c'est epsilon, c'est forcément vrai
    return True, count


def fonction_EXPR2(token_list, count):  # EXPR2 ::= EXPR3 / EXPR2 ::= 270 EXPR3
    # EXPR2 ::= EXPR3
    count_tmp = count
    result = rec(['EXPR3'], token_list, count_tmp, count, 0)
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


def fonction_EXPR3(token_list, count):  # EXPR3 ::= EXPR4 EXPRC
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
    # todo vérifier le caractère après 47
    count_tmp = count
    result = rec([47, 61, 'EXPR4', 'EXPRC'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # si c'est epsilon, c'est forcément vrai
    return True, count


def fonction_EXPR4(token_list, count):  # EXPR4 ::= EXPR5 EXPRE
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


def fonction_EXPRE1(token_list, count):  # EXPRE1 ::= EXPR5 EXPRE / EXPRE1 ::= 61 EXPR5 EXPRE
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


def fonction_EXPRE2(token_list, count):  # EXPRE2 ::= EXPR5 EXPRE / EXPRE2 ::= 61 EXPR5 EXPRE
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


def fonction_EXPR5(token_list, count):  # EXPR5 ::= EXPR6 EXPRF
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


def fonction_EXPR6(token_list, count):  # EXPR6 ::= EXPR7 EXPRG
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
    # todo vérifier le caractère après 47
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
    result = rec(['EXPR8'], token_list, count_tmp, count, 0)
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


def fonction_EXPR8(token_list, count):  # EXPR8 ::= N11
    count_tmp = count
    result = rec(['N11'], token_list, count_tmp, count, 0)
    if result[0]:  # N11
        count = result[1]
        return True, count

    return False, count


def fonction_A10(token_list, count):  # A10 ::= N8 A102
    count_tmp = count
    result = rec(['N8', 'A102'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    return False, count


def fonction_A102(token_list, count):  # A102 ::= '' / A102 ::= 44 A10
    count_tmp = count
    result = rec([44], token_list, count_tmp, count, 0)
    if result[0]:  # ,
        count_tmp = result[1]
        result = rec(['A10'], token_list, count_tmp, count, 0)
        if result[0]:  # A10
            count = result[1]
            return True, count

        # si on a lu, et que l'on se rend compte qu'il ne fallait pas
        return False, count

    # cas où c'est espilon donc forcément vrai
    return True, count


def fonction_N9(token_list, count):
    # N9 ::= 286 46 285 58 61 N8 59
    # N9 ::= N16 46 285 58 61 N8 59
    # N9 ::= 280 46 285 58 61 N8 59
    # N9 ::= 262 46 285 58 61 N8 59
    # N9 ::= 271 46 285 58 61 N8 59
    # N9 ::= 40 N8 41 46 285 58 61 N8 59
    # N9 ::= 269 285 46 285 58 61 N8 59
    # N9 ::= 287 34 288 40 N8 41 46 285 58 61 N8 59
    # N9 ::= EXPR1 EXPRA 46 285 58 61 N8 59
    # N9 ::= 285 N92
    # N9 ::= 277 A11 59
    # N9 ::= 258 A2 261 59
    # N9 ::= 265 N8 279 A2 A12 A13 261 265 59
    # N9 ::= 263 285 266 A14 N8 46 46 N8 268 A2 261 268 59
    # N9 ::= 283 N8 268 A2 261 268 59

    # N9 ::= 286 46 285 58 61 N8 59
    count_tmp = count
    result = rec([286, 46, 285, 58, 61, 'N8', 59], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # N9 ::= N16 46 285 58 61 N8 59
    count_tmp = count
    result = rec(['N16', 46, 285, 58, 61, 'N8', 59], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # N9 ::= 280 46 285 58 61 N8 59
    count_tmp = count
    result = rec([280, 46, 285, 58, 61, 'N8', 59], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # N9 ::= 262 46 285 58 61 N8 59
    count_tmp = count
    result = rec([262, 46, 285, 58, 61, 'N8', 59], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # N9 ::= 271 46 285 58 61 N8 59
    count_tmp = count
    result = rec([271, 46, 285, 58, 61, 'N8', 59], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # N9 ::= 40 N8 41 46 285 58 61 N8 59
    count_tmp = count
    result = rec([40, 'N8', 41, 46, 285, 58, 61, 'N8', 59], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # N9 ::= 269 285 46 285 58 61 N8 59
    count_tmp = count
    result = rec([269, 285, 46, 285, 58, 61, 'N8', 59], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # N9 ::= 287 34 288 40 N8 41 46 285 58 61 N8 59
    count_tmp = count
    result = rec([287, 34, 288, 40, 'N8', 41, 46, 285, 58, 61, 'N8', 59], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # N9 ::= EXPR1 EXPRA 46 285 58 61 N8 59
    count_tmp = count
    result = rec(['EXPR1', 'EXPRA', 46, 285, 58, 61, 'N8', 59], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # N9 ::= 285 N92
    count_tmp = count
    result = rec([285, 'N92'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # N9 ::= 277 A11 59
    count_tmp = count
    result = rec([277, 'A11', 59], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # N9 ::= 258 A2 261 59
    count_tmp = count
    result = rec([258, 'A2', 261, 59], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # N9 ::= 265 N8 279 A2 A12 A13 261 265 59
    count_tmp = count
    result = rec([265, 'N8', 279, 'A2', 'A12', 'A13', 261, 265, 59], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # N9 ::= 263 285 266 A14 N8 46 46 N8 268 A2 261 268 59
    count_tmp = count
    result = rec([263, 285, 266, 'A14', 'N8', 46, 46, 'N8', 268, 'A2', 261, 268, 59], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # N9 ::= 283 N8 268 A2 261 268 59
    count_tmp = count
    result = rec([283, 'N8', 268, 'A2', 261, 268, 59], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    return False, count


def fonction_N92(token_list, count):
    # N92 ::= 40 A10 41 N93
    # N92 ::= 58 61 N8 59
    # N92 ::= 59

    # N92 ::= 40 A10 41 N93
    count_tmp = count
    result = rec([40, 'A10', 41, 'N93'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # N92 ::=  58 61 N8 59
    count_tmp = count
    result = rec([58, 61, 'N8', 59], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # N92 ::= 59
    count_tmp = count
    result = rec([59], token_list, count_tmp, count, 0)
    if result[0]:  # ;
        count = result[1]
        return True, count

    return False, count


def fonction_N93(token_list, count):  # N93 ::= 46 285 58 61 N8 59 / N93 ::= 59
    # N93 ::= 46 285 58 61 N8 59
    count_tmp = count
    result = rec([46, 285, 58, 61, 'N8', 59], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # N93 ::= 59
    count_tmp = count
    result = rec([59], token_list, count_tmp, count, 0)
    if result[0]:  # ;
        count = result[1]
        return True, count

    return False, count


def fonction_A11(token_list, count):  # A11 ::= '' / A11 ::= N8
    # A11 ::= N8
    count_tmp = count
    result = rec(['N8'], token_list, count_tmp, count, 0)
    if result[0]:  # N8
        count = result[1]
        return True, count

    return False, count


def fonction_A12(token_list, count):  # A12 ::= '' / A12 ::= 260 N8 279 A2 A12
    # A12 ::= 260 N8 279 A2 A12
    count_tmp = count
    result = rec([260, 'N8', 279, 'A2', 'A12'], token_list, count_tmp, count, 0)
    if result[0]:  # 260 N8 279 A2 A12
        count = result[1]
        return True, count

    # si c'est epsilon, c'est forcément vrai
    return True, count


def fonction_A13(token_list, count):  # A13 ::= '' / A13 ::= 259 A2
    # A13 ::= 259 A2
    count_tmp = count
    result = rec([259, 'A2'], token_list, count_tmp, count, 0)
    if result[0]:  # 259 A2
        count = result[1]
        return True, count

    # si c'est epsilon, c'est forcément vrai
    return True, count


def fonction_N11(token_list, count):  # N11 ::= 285 N111
    # N11 ::= 285 N111
    count_tmp = count
    result = rec([285, 'N111'], token_list, count_tmp, count, 0)
    if result[0]:  # 285 N111
        count = result[1]
        return True, count

    return False, count


def fonction_N111(token_list, count):  # N111 ::= '' / N111 ::= 46 285
    # N111 ::= 46 285
    count_tmp = count
    result = rec([46, 285], token_list, count_tmp, count, 0)
    if result[0]:  # 46 285
        count = result[1]
        return True, count

    # si c'est epsilon, c'est forcément vrai
    return True, count


def fonction_N12(token_list, count):  # N12 ::= tchiffre
    # 48, 49, 50, 51, 52, 53, 54, 55, 56, 57
    count_tmp = count
    result = rec([48], token_list, count_tmp, count, 0)  # 0
    if result[0]:  # 0
        count = result[1]
        return True, count

    count_tmp = count
    result = rec([49], token_list, count_tmp, count, 0)  # 1
    if result[0]:  # 1
        count = result[1]
        return True, count

    count_tmp = count
    result = rec([50], token_list, count_tmp, count, 0)  # 2
    if result[0]:  # 2
        count = result[1]
        return True, count

    count_tmp = count
    result = rec([51], token_list, count_tmp, count, 0)  # 3
    if result[0]:  # 3
        count = result[1]
        return True, count

    count_tmp = count
    result = rec([52], token_list, count_tmp, count, 0)  # 4
    if result[0]:  # 4
        count = result[1]
        return True, count

    count_tmp = count
    result = rec([53], token_list, count_tmp, count, 0)  # 5
    if result[0]:  # 5
        count = result[1]
        return True, count

    count_tmp = count
    result = rec([54], token_list, count_tmp, count, 0)  # 6
    if result[0]:  # 6
        count = result[1]
        return True, count

    count_tmp = count
    result = rec([55], token_list, count_tmp, count, 0)  # 7
    if result[0]:  # 7
        count = result[1]
        return True, count

    count_tmp = count
    result = rec([56], token_list, count_tmp, count, 0)  # 8
    if result[0]:  # 8
        count = result[1]
        return True, count

    count_tmp = count
    result = rec([57], token_list, count_tmp, count, 0)  # 9
    if result[0]:  # 9
        count = result[1]
        return True, count

    return False, count


def fonction_N13(token_list, count):  # N13 ::= tlettre
    print(""
          ""
          ""
          ""
          ""
          ""
          ""
          ""
          "")
    # 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
    # 90, 91, 92, 93, 94, 95, 96
    # 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118,
    # 119, 120, 121, 122
    count_tmp = count
    result = rec([65], token_list, count_tmp, count, 0)  # A
    if result[0]:  # A
        count = result[1]
        return True, count

    count_tmp = count
    result = rec([66], token_list, count_tmp, count, 0)  # B
    if result[0]:  # B
        count = result[1]
        return True, count

    count_tmp = count
    result = rec([67], token_list, count_tmp, count, 0)  # C
    if result[0]:  # C
        count = result[1]
        return True, count

    count_tmp = count
    result = rec([68], token_list, count_tmp, count, 0)  # D
    if result[0]:  # D
        count = result[1]
        return True, count

    count_tmp = count
    result = rec([69], token_list, count_tmp, count, 0)  # E
    if result[0]:  # E
        count = result[1]
        return True, count

    # todo le faire pour toutes les lettres

    return False, count


# def fonction_N15(token_list, count):  # N15 ::= N12 A15
    # N15 ::= N12 A15
    # count_tmp = count
    # result = rec(['N12', 'A15'], token_list, count_tmp, count, 0)
    # if result[0]:  # N12 A15
        # count = result[1]
        # return True, count

    # return False, count


def fonction_A15(token_list, count):  # A15 ::= '' / A15 ::= 286
    # A15 ::= N12 A15
    count_tmp = count
    result = rec([286], token_list, count_tmp, count, 0)
    if result[0]:  # N12 A15
        count = result[1]
        return True, count

    # si c'est epsilon, c'est forcément vrai
    return True, count


def fonction_N16(token_list, count):  # N16 ::= 34 A16 34
    # N16 ::= 34 A16 34
    count_tmp = count
    result = rec([34, 'A16', 34], token_list, count_tmp, count, 0)
    if result[0]:  # 34 A16 34
        count = result[1]
        return True, count

    return False, count


def fonction_A16(token_list, count):
    # A16 ::= N12
    # A16 ::= N13
    # A16 ::= 44
    # A16 ::= 58
    # A16 ::= 40
    # A16 ::= 41
    # A16 ::= 45
    # A16 ::= 61
    # A16 ::= 60
    # A16 ::= 62
    # A16 ::= 43
    # A16 ::= 42
    # A16 ::= 47
    # A16 ::= 46
    # A16 ::= 95
    # A16 ::= 34

    # A16 ::= N12
    count_tmp = count
    result = rec(['N12'], token_list, count_tmp, count, 0)
    if result[0]:  # N12
        count = result[1]
        return True, count

    # A16 ::= N13
    count_tmp = count
    result = rec([285], token_list, count_tmp, count, 0)
    if result[0]:  # N13
        count = result[1]
        return True, count

    # A16 ::= 44
    count_tmp = count
    result = rec([44], token_list, count_tmp, count, 0)
    if result[0]:  # ,
        count = result[1]
        return True, count

    # A16 ::= 58
    count_tmp = count
    result = rec([58], token_list, count_tmp, count, 0)
    if result[0]:  # :
        count = result[1]
        return True, count

    # A16 ::= 40
    count_tmp = count
    result = rec([40], token_list, count_tmp, count, 0)
    if result[0]:  # (
        count = result[1]
        return True, count

    # A16 ::= 41
    count_tmp = count
    result = rec([41], token_list, count_tmp, count, 0)
    if result[0]:  # )
        count = result[1]
        return True, count

    # A16 ::= 45
    count_tmp = count
    result = rec([45], token_list, count_tmp, count, 0)
    if result[0]:  # -
        count = result[1]
        return True, count

    # A16 ::= 61
    count_tmp = count
    result = rec([61], token_list, count_tmp, count, 0)
    if result[0]:  # =
        count = result[1]
        return True, count

    # A16 ::= 60
    count_tmp = count
    result = rec([60], token_list, count_tmp, count, 0)
    if result[0]:  # <
        count = result[1]
        return True, count

    # A16 ::= 62
    count_tmp = count
    result = rec([62], token_list, count_tmp, count, 0)
    if result[0]:  # >
        count = result[1]
        return True, count

    # A16 ::= 43
    count_tmp = count
    result = rec([43], token_list, count_tmp, count, 0)
    if result[0]:  # +
        count = result[1]
        return True, count

    # A16 ::= 42
    count_tmp = count
    result = rec([42], token_list, count_tmp, count, 0)
    if result[0]:  # *
        count = result[1]
        return True, count

    # A16 ::= 47
    # todo vérifier le caractère d'après 47
    count_tmp = count
    result = rec([47], token_list, count_tmp, count, 0)
    if result[0]:  # /
        count = result[1]
        return True, count

    # A16 ::= 46
    count_tmp = count
    result = rec([46], token_list, count_tmp, count, 0)
    if result[0]:  # .
        count = result[1]
        return True, count

    # A16 ::= 95
    count_tmp = count
    result = rec([95], token_list, count_tmp, count, 0)
    if result[0]:  # _
        count = result[1]
        return True, count

    # A16 ::= 34
    count_tmp = count
    result = rec([34], token_list, count_tmp, count, 0)
    if result[0]:  # "
        count = result[1]
        return True, count

    return False, count


def fonction_A14(token_list, count):  # A14 ::= '' / A14 ::= 278
    count_tmp = count
    result = rec([278], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    # si c'est epsilon, c'est forcément vrai
    return True, count
