# import du dictionnaire
from dictionnaire import *

def get_token(name_file):
    # ouverture du fichier
    file = open(name_file, "r")
    # initialisation de la liste de token
    token_list = []

    # lecture du fichier caractère par caractère
    
    for ligne in file:
        actual_char = ''
        for char in ligne:

            #print(char)

            # si le caractère est un espace, un retour à la ligne ou un tab ou une balise de commentaire, on passe au caractère suivant, 
            # A MODIF SI ON CONSIDERE ID : 
            # if char == " " or char == "\n" or char == "\t" or char == '#' or char not in [a-z A-Z 0-1] ou ajouter une variable peak et faire comme dans le bouquin:
            if char == " " or char == "\n" or char == "\t" or char == '#':

                # l'un des cas au dessus signifie que l'on change de token
                #si il s'agit d'un token reconnu(dans le dico), on ajoute sa valeur à la token_list
                if term.__contains__(actual_char) and actual_char != '':
                    #print('ajout dans tl de :', term.get(actual_char), 'correspondant à :', actual_char)
                    token_list.append(term.get(actual_char))
                

                #si il n'est pas reconnu on ajoute le code ASCII de chaque caractère dans la token_list
                else :   
                      
                    for chara in actual_char :
                            #print('ajout dans token_list de :', term.get(chara), 'correspondant à :', chara)
                            token_list.append(term.get(chara))

# A MODIF SI ON CONSIDERE ID : 
#                   token_list.append((term.get('id'), actual_char)
                
                #print('on reset')
                actual_char = ''
                
                continue

            # dans le cas où on rencontre un autre caractère que espace, retour à la ligne ou un tab alors on l'ajoute au token en train d'être lu actuellement 
            else :
                actual_char += char
                #print('char actuel =', actual_char)
                continue

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

    #print(token_list)

    # fermeture du fichier
    file.close()
    return token_list

#get_token("exemple.ada")

#print(term.get('.'))
#print(term.__contains__('.'))