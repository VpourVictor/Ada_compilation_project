# import du dictionnaire
import dictionnaire_ter as dictionnaire_ter

# definition d'une fonction qui gère un string de char découpé dans la partie 1 de get_token
def treat_a_string(string, token_list) :
    term = dictionnaire_ter.term
    if string != '' :
        # s'il s'agit d'un token reconnu (dans le dico), on ajoute sa valeur à la token_list
        if term.__contains__(string):
            # print('ajout dans tl de :', term.get(string), 'correspondant à :', string)
            token_list.append(term.get(string))

        # cas des 'id', c'est-à-dire un mot avec des lettres, des chiffres et des '_'
        elif string[0].isalpha() :
            len_str = len(string)
            i = 0

            while i < len_str and (string[i].isalpha() or string[i].isdigit() or string[i] == '_' or string[i] == '0')  :
                i += 1
            
            if i == len_str :
                token_list.append((term.get('id'), string))
            else :
                token_list.append((term.get('id'), string[:i]))
                # appel récursif
                treat_a_string(string[i:], token_list )
        
        # cas des num (entiers)
        elif string[0].isdigit() :
            len_str = len(string)
            i = 0

            while i < len_str and (string[i].isdigit() or string[i] == '0'):
                i += 1

            if i == len_str :
                token_list.append((term.get('num'), string))
            else :
                token_list.append((term.get('num'), string[:i]))
                # appel récursif
                treat_a_string(string[i:], token_list )

        # autre (donc '(' , ')' , '*', '+' etc...)
        else :
            token_list.append(term.get(string[0]))
            treat_a_string(string[1:], token_list )

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

    # lecture du fichier
    for ligne in file:
        actual_char = ''
        l = len(ligne)
        i = 0
        while i < l :
            # print(char)
            # si le caractère est un espace, un retour à la ligne ou un tab ou une balise de commentaire,
            # on passe au caractère suivant,
            if ligne[i] == " " or ligne[i] == "\n" or ligne[i] == "\t" or ligne[i] == '#':
                # on peut mettre autant d'espace/tab/ligne qu'on veut
                if actual_char != '' :
                    list_char.append(actual_char)
                    actual_char = ''
                i += 1

            # cas du commentaire : on ne lit plus la ligne
            elif ligne[i] == '-' and i != l-1 and ligne[i+1] == '-' :
                if actual_char != '' :
                    list_char.append(actual_char)
                    actual_char = ''
                i = l

            # dans le cas où on rencontre un autre caractère que 'espace, retour à la ligne ou tab'
            # alors on l'ajoute au token en train d'être lu actuellement
            elif i == l-1 :
                print("dans ce cas là i = l et actual_char =", actual_char)
                actual_char += ligne[i]
                list_char.append(actual_char)
                actual_char = ''
                break
            
            else :
                actual_char += ligne[i]
                i += 1
                print('char actuel =', actual_char)

    print(list_char)
    # Cette deuxième partie ajoute les tokens à la liste des tokens
    for string in list_char :
        treat_a_string(string, token_list)
            

    # transformation des caractères du fichier en liste de token
    # par rapport au dictionnaire
    # on retourne une liste de token

    # si la chaîne est un identifiant (ex : if) on le remplacera directement par le code associé
    # si caractère de commentaire, on supprime ce qui est avant la balise de commentaire /* ... */

    # exemple : with = 284
    # A = 65
    # I = 79

    # si pas d'espace
    # on lit tout, si le total n'est pas dans le dictionnaire,
    # on reconnait : séparément les caractères

    print(token_list)

    # fermeture du fichier
    #file.close()
    
    return token_list

get_token(".\exemples\exemple_if.ada")
