from lexeur.dictionnaire_ter import term2

dico = term2


def compare(p_attendu, p_reel):
    """return si moins de 2 diff entre p1 et les lettres de p2"""
    global dico
    if type(p_reel) == int and type(p_attendu) == int:
        return p_reel == p_attendu

    elif type(p_reel) == int:  # cas où on attendait un id ou nbr spécifique
        if p_attendu[0] == 286:  # on attendait un nombre
            return False
        else:  # on attend un identifiant
            mot_reel = dico.get(p_reel)  # a modif proprement
            mot_attendu = p_attendu[1]
            return compare_string(mot_reel, mot_attendu)

    elif type(p_attendu) == int:  # cas où on a un id ou nbr spécifique
        if p_reel[0] == 286:  # on a un nombre
            return False
        else:  # on a un identifiant
            mot_reel = p_reel[1]  # a modif proprement

            mot_attendu = dico.get(p_attendu)
            return compare_string(mot_reel, mot_attendu)

    else:  # cas où les deux sont 285 ou 286
        if p_attendu[0] == 286 and p_reel[0] == 285:  # on attendait un nombre, mais on a eu un id
            return False
        elif p_attendu[0] == p_reel[0]:  # deux id ou deux nombres
            return compare_string(p_attendu[1], p_reel[1])
        else:  # attendu est id, obtenu est un nombre
            return compare_string(p_attendu[1], p_reel[1])


def compare_string(chaine1, chaine2):
    if abs(len(chaine1) - len(chaine2)) > 1:
        return False
    differences = 0
    i, j = 0, 0
    while i < len(chaine1) and j < len(chaine2):
        if chaine1[i] != chaine2[j]:
            differences += 1
            if len(chaine1) > len(chaine2):
                i += 1
            elif len(chaine1) < len(chaine2):
                j += 1
            else:
                i += 1
                j += 1
        else:
            # Les caractères sont identiques, passer au suivant
            i += 1
            j += 1
    differences += abs(len(chaine1) - i) + abs(len(chaine2) - j)
    return differences < 2 or atMostSwitch(chaine1, chaine2)


def atMostSwitch(chaine1, chaine2):
    if len(chaine1) != len(chaine2):
        return False
    differences = 0
    positions_differentes = []
    for i, (char1, char2) in enumerate(zip(chaine1, chaine2)):
        if char1 != char2:
            differences += 1
            positions_differentes.append(i)
    return (differences == 2 and positions_differentes[0] + 1 == positions_differentes[1] and chaine1[
        positions_differentes[0]] == chaine2[positions_differentes[1]] and chaine1[positions_differentes[1]] == chaine2[
                positions_differentes[0]]) or differences == 0
