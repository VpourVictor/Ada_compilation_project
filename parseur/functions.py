from parseur.reader_carac import reader_carac


def fonction_N1(token_list):  # N1 ::= 284 285 46 285 59 282 285 46 285 59 274 285 267 A1 258 A2 261 A3 59
    count = 0
    count_tmp = count
    result = reader_carac(284, token_list, count_tmp, count) # with
    if result[0]:  # with
        count_tmp = result[1]
        if reader_carac((285, 'Ada'), token_list, count_tmp, count)[0]:  # id
            count_tmp = reader_carac(46, token_list, count_tmp, count)[1]
            if reader_carac(46, token_list, count_tmp, count)[0]:  # .
                count_tmp = reader_carac(285, token_list, count_tmp, count)[1]
                if reader_carac(285, token_list, count_tmp, count)[0]:  # id
                    count_tmp = reader_carac(59, token_list, count_tmp, count)[1]
                    if reader_carac(59, token_list, count_tmp, count)[0]: # ;
                        count_tmp = reader_carac(282, token_list, count_tmp, count)[1]
                        """if reader_carac(282, token_list, count_tmp, count)[0]: # use
                            count_tmp = reader_carac(282, token_list, count_tmp, count)[1]
                            if reader_carac(285, token_list, count_tmp, count)[0]: # id
                                count_tmp = reader_carac(285, token_list, count_tmp, count)[1]
                                if reader_carac(46, token_list, count_tmp, count)[0]: # .
                                    count_tmp = reader_carac(46, token_list, count_tmp, count)[1]
                                    if reader_carac(285, token_list, count_tmp, count)[0]: # id
                                        count_tmp = reader_carac(285, token_list, count_tmp, count)[1]
                                        if reader_carac(59, token_list, count_tmp, count)[0]: # ;
                                            count_tmp = reader_carac(59, token_list, count_tmp, count)[1]
                                            if reader_carac(274, token_list, count_tmp, count)[0]: # procedure
                                                count_tmp = reader_carac(274, token_list, count_tmp, count)[1]
                                                if reader_carac(285, token_list, count_tmp, count)[0]: # id
                                                    count_tmp = reader_carac(285, token_list, count_tmp, count)[1]
                                                    if reader_carac(267, token_list, count_tmp, count)[0]: # is
                                                        count_tmp = reader_carac(267, token_list, count_tmp, count)[1]
                                                        """ """if fonction_A1(token_list, count)[0]: # A1
                                                            count = fonction_A1(token_list, count_tmp, count)[2]
                                                            if reader_carac(258, token_list, count_tmp, count)[0]: # begin
                                                                count_tmp = reader_carac(258, token_list, count_tmp, count)[1]
                                                                if fonction_A2(token_list, count)[0]: # A2
                                                                    count = fonction_A2(token_list, count_tmp, count)[2]
                                                                    if reader_carac(261, token_list, count_tmp, count)[0]: # end
                                                                        count_tmp = reader_carac(261, token_list, count_tmp, count)[1]
                                                                        if fonction_A3(token_list):
                                                                            count = fonction_A3(token_list, count_tmp, count)[2]
                                                                            if reader_carac(59, token_list, count_tmp, count):
                                                                                count_tmp = reader_carac(59, token_list, count_tmp, count)[1]"""
                        count = count_tmp
                        return True, count_tmp, count
    return False, count_tmp, count

"""
def fonction_A1(token_list, count):  # A1 ::= '' / A1 ::= N2 A1
    count_tmp = count
    if fonction_N2(token_list, count_tmp)[0]:  # N2
        count = fonction_A1(token_list, count_tmp)[2]
        if fonction_A1(token_list, count_tmp)[0]:  # A1
            count = fonction_A1(token_list, count_tmp)[2]
            return True, count_tmp, count
        count_tmp = count
        return False, count_tmp, count
    count_tmp = count
    return True, count_tmp, count
"""


"""
def fonction_N16(token_list, count):  # N16 ::= 34 A16 34
    # au départ la valeur du compteur temporai est égale à celle du compteur actuel
    count_tmp = count
    if reader_carac(34, token_list, count_tmp, count)[0]:  # 34
        count_tmp = reader_carac(34, token_list, count_tmp, count)[1]
        if fonction_A16(token_list, count)[0]:  # A16
            count = fonction_N16(token_list, count_tmp)[2]
            if reader_carac(34, token_list, count_tmp, count)[0]:  # 34
                count = count_tmp
                return True, count_tmp, count
        else:
            count = count_tmp
    return False, count_tmp, count
"""