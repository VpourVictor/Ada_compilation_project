from parseur.arbre import Noeud


def fichier(list_token):
    # création de la racine de l'arbre
    racine = Noeud("fichier")

    # fonction à compléter avec le reste de la règle N1
    if list_token[0] == 284:  # 284 = with
        # corriger et faire appel à Term
        racine.add(Noeud("with"))
        if ident_ada(list_token[1]):  # 285 = Ada
            racine.add(Noeud(""))
            if list_token[2] == 46:  # 46 = .
                racine.add(Noeud("."))
                if ident_text_io(list_token[3]):  # 285 = Text_IO
                    racine.add(Noeud(""))
                    if list_token[4] == 59:  # 59 = ;
                        racine.add(Noeud(";"))
                        return True
    else:
        # corriger et signaler les erreurs
        return False


def ident_ada(couple):
    if couple[0] == 285 and couple[1] == "Ada":
        return True
    else:
        return False


def ident_text_io(couple):
    if couple[0] == 285 and couple[1] == "Text_IO":
        return True
    else:
        return False
