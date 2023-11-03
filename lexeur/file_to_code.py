# import du dictionnaire
from dictionnaire import *

def get_token(name_file):
    # ouverture du fichier
    file = open(name_file, "r")
    # initialisation de la liste de token
    token_list = []

    # lecture du fichier caractère par caractère
    for ligne in file:
        for char in ligne:
            print(char)

            # si le caractère est un espace, on passe au caractère suivant
            if char == " ":
                continue
            # si le caractère est un retour à la ligne, on passe au caractère suivant
            elif char == "\n":
                continue
            # si le caractère est un tab, on passe au caractère suivant
            elif char == "\t":
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

    # fermeture du fichier
    file.close()
