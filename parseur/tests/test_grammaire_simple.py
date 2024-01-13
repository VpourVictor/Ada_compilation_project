from parseur.reader_carac import reader_carac


def switch_fonction(name, token_list, count_tmp):
    result = None
    match name:
        case 'X':
            result = fonction_X(token_list, count_tmp)
        case 'Y':
            result = fonction_Y(token_list, count_tmp)
        case 'Z':
            result = fonction_Z(token_list, count_tmp)

        case '.':
            result = False, count_tmp

    return result


def rec(list_att, token_list, count_tmp, count, local):
    print("Liste att")
    print(list_att)
    print("local")
    print(local)
    print("count_tmp")
    print(count_tmp)

    if count_tmp == token_list.__len__():
        print("c'est fini")
        return True, count_tmp

    if type(list_att[local]) == int:
        result = reader_carac(list_att[local], token_list, count_tmp)  # with
        if result[0]:  # with
            count_tmp = result[1]
            print("c'est good")
            return rec(list_att, token_list, count_tmp, count, local + 1)
    else:
        print(list_att[local])
        result = switch_fonction(list_att[local], token_list, count_tmp)
        print(result)
        print("iciiii")
        if result[0]:
            print("dedans")
            count = result[1]
            count_tmp = count
            return rec(list_att, token_list, count_tmp, count, local + 1)

    # voir si c'est vraiment bien ca la fin (true ou false)
    return False, count

def fonction_S(token_list):  # XY
    count = 0
    count_tmp = count
    return rec(['X', 'Y'], token_list, count_tmp, count, 0)


def fonction_X(token_list, count):  # X ::= aXb / X ::= ''
    count_tmp = count
    result = reader_carac(1, token_list, count_tmp)
    print("deb")
    print(result)
    if result[0]:  # a
        count_tmp = result[1]
        result = fonction_X(token_list, count_tmp)
        if result[0]:  # X
            count = result[1]
            result = reader_carac(2, token_list, count)
            if result[0]:  # b
                count = result[1]
                return True, count

        # si on a lu a et que l'on se rend compte qu'il ne fallait pas
        return False, count

    # cas où c'est espilon donc forcément vrai
    return True, count


def fonction_Y(token_list, count):  # Y ::= cZ  / Y ::= Ze
    count_tmp = count
    result = rec([3, 'Z'], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    count_tmp = count
    result = rec(['Z', 5], token_list, count_tmp, count, 0)
    if result[0]:
        count = result[1]
        return True, count

    return False, count


def fonction_Z(token_list, count):  # Z ::= dcZ / Z ::= ''
    count_tmp = count
    result = reader_carac(4, token_list, count_tmp)
    print("j'ai lu 4")
    print(result)
    if result[0]:  # d
        count_tmp = result[1]
        result = reader_carac(3, token_list, count_tmp)
        print("j'ai lu 3")
        print(result)
        if result[0]:  # c
            count_tmp = result[1]
            result = fonction_Z(token_list, count_tmp)
            if result[0]:  # Z
                count = result[1]
                return True, count

        # si on a lu dc et que l'on se rend compte qu'il ne fallait pas
        return False, count

    # cas où c'est espilon donc forcément vrai
    return True, count


if __name__ == '__main__':
    token_list = [1, 2, 4, 3, 5]
    print(token_list)
    print(fonction_S(token_list))

    token_list = [1, 2, 2, 1, 2]
    print(token_list)
    print(fonction_S(token_list))
