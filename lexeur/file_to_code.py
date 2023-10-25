# import du dictionnaire

# lecture du fichier à reconnaitre
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