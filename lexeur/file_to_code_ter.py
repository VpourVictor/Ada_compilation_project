# import du dictionnaire
import dictionnaire_ter as dictionnaire_ter


# definition d'une fonction qui gère un string de char découpé dans la partie 1 de get_token
def treat_a_string(string, token_list):
    term = dictionnaire_ter.term
    if string != '':
        # s'il s'agit d'un token reconnu (dans le dico), on ajoute sa valeur à la token_list
        if term.__contains__(string):
            # print('ajout dans tl de :', term.get(string), 'correspondant à :', string)
            token_list.append(term.get(string))

        # cas des 'id', c'est-à-dire un mot avec des lettres, des chiffres et des '_'
        elif string[0].isalpha():
            len_str = len(string)
            i = 0

            while i < len_str and (string[i].isalpha() or string[i].isdigit() or string[i] == '_' or string[i] == '0'):
                i += 1

            if i == len_str:
                if term.__contains__(string):
                    token_list.append(term.get(string))
                else:
                    token_list.append((term.get('id'), string))
            else:
                if term.__contains__(string[:i]):
                    token_list.append(term.get(string[:i]))
                else:
                    token_list.append((term.get('id'), string[:i]))
                # appel récursif
                treat_a_string(string[i:], token_list)

        # cas des num (entiers)
        elif string[0].isdigit():
            len_str = len(string)
            i = 0

            while i < len_str and (string[i].isdigit() or string[i] == '0'):
                i += 1

            if i == len_str:
                token_list.append((term.get('num'), string))
            else:
                if term.__contains__(string[:i]):
                    token_list.append(term.get(string[:i]))
                else:
                    token_list.append((term.get('num'), string[:i]))

                # appel récursif
                treat_a_string(string[i:], token_list)

        # autre (donc '(' , ')' , '*', '+' etc...)
        elif string[0] in dictionnaire_ter.cle:
            token_list.append(term.get(string[0]))
            treat_a_string(string[1:], token_list)

        else:
            # si on arrive ici, c'est qu'on a un caractère non reconnu
            print('erreur : caractère non reconnu :', string[0])

    return token_list


# fonction qui transforme un fichier en liste de token
def get_token(name_file):
    # ouverture du fichier
    file = open(name_file, "r")
    # initialisation de la liste de token
    token_list = []

    # list_char correspond à l'ensemble des unités de char qui ne sont pas des commentaires
    # et qui sont séparées par des espaces, des retours à la ligne ou des tabulations

    # Cette première partie permet d'enlever les espaces/tab/commentaires
    list_char = []

    num_line = 1
    # lecture du fichier
    for ligne in file:
        actual_char = ''
        l = len(ligne)
        i = 0
        while i < l:
            # print(char)
            # si le caractère est un espace, un retour à la ligne ou un tab ou une balise de commentaire,
            # on passe au caractère suivant,
            if ligne[i] == " " or ligne[i] == "\n" or ligne[i] == "\t":
                # on peut mettre autant d'espace/tab/ligne qu'on veut
                if actual_char != '':
                    list_char.append(actual_char)
                    actual_char = ''
                i += 1

            # cas du commentaire : on ne lit plus la ligne
            elif ligne[i] == '-' and i != l - 1 and ligne[i + 1] == '-':
                if actual_char != '':
                    list_char.append(actual_char)
                    actual_char = ''
                i = l

            # si on est à la fin de la dernière ligne
            elif i == l - 1:
                actual_char += ligne[i]
                list_char.append(actual_char)
                break

            elif ligne[i] not in dictionnaire_ter.cle:
                # print(ord(ligne[i]))
                # print(chr(172))

                print('erreur : caractère ' + ligne[i] + ' non reconnu à la ligne ' + str(num_line))
                # on incrémente quand même i pour ne pas rester bloqué sur le caractère non reconnu
                # choix de passer à la suite (ignorer le caractère non reconnu)
                i += 1

            # dans le cas où on rencontre un autre caractère que 'espace, retour à la ligne ou tab'
            # ou caractère non reconnu
            # alors on l'ajoute au token en train d'être lu actuellement
            else:
                actual_char += ligne[i]
                i += 1

        num_line += 1

    # print(list_char)
    # Cette deuxième partie ajoute les tokens à la liste des tokens
    for string in list_char:
        treat_a_string(string, token_list)

    for i in range(len(token_list)):
        if token_list[i] in [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
          87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116,
                                   117, 118, 119, 120, 121, 122]:
            token_list[i] = (285, chr(token_list[i]))
        if token_list[i] in [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]:
            token_list[i] = (286, chr(token_list[i]))

    return token_list

