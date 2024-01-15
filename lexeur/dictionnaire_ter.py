# définition du dictionnaire contenant les 95 caractères imprimables
# de la table ASCII et les mots clés du langage Ada

# initialisation du dictionnaire vide
term = {}
term2 = {}
# tableau contenant l'ensemble des caractères et mots clés reconnus par le lexeur
cle = ['!', '\'', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/',
       '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
       ':', ';', '<', '=', '>', '?', '@',
       'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
       'W', 'X', 'Y', 'Z',
       '[', ']', '', '^', '_', '`',
       'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z',
       '{', '|', '}', '~',
       'access', 'and', 'begin', 'else', 'elsif', 'end', 'false', 'for', 'function', 'if', 'in', 'is', 'loop', 'new',
       'not', 'null', 'or', 'out', 'procedure', 'record', 'rem', 'return', 'reverse', 'then', 'true', 'type', 'use',
       'while', 'with', 'id', 'num', 'character', 'val']

# tableau contenant les codes associés aux caractères et mots clés
valeur = [
    # '!', '\'', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/',
      33,   34,   35,  36, 37,  38,   40, 41,   42,  43,  44,  45,  46,  47,
    # '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
       48,  49,  50,  51,  52,  53,  54,  55,  56,  57,
    # ':', ';', '<', '=', '>', '?', '@',
       58,  59,  60,  61,  62,  63,  64,
    # 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
      65,  66,  67,   68,  69,  70,  71,  72,  73,  74,  75,  76,  77,  78,  79,  80,  81,  82,  83,  84,  85,  86,
    # 'W', 'X', 'Y', 'Z',
      87,  88,  89,   90,
    # '[', ']', '', '^', '_', '`',
       91,  92, 93,  94,  95,  96,
    # 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       97,  98,  99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118,
    # 'w', 'x', 'y', 'z',
      119, 120, 121, 122,
    # '{', '|', '}', '~',
      123, 124, 125, 126,
    # 'access', 'and', 'begin', 'else', 'elsif', 'end', 'false', 'for', 'function', 'if', 'in', 'is', 'loop', 'new',
        256,     257,    258,     259,    260,    261,    262,    263,       264,    265,  266,  267,   268,   269,
    # 'not', 'null', 'or', 'out', 'procedure', 'record', 'rem', 'return', 'reverse', 'then', 'true', 'type', 'use',
       270,   271,   272,   273,      274,        275,    276,     277,       278,     279,    280,    281,    282,
    # 'while', 'with', 'id', 'num', 'character', 'val']
        283,     284,   285,   286,      287,     288]

# remplissage du dictionnaire
for i in range(len(cle)):
    term[cle[i]] = valeur[i]

for i in range(len(valeur)):
    term2[valeur[i]] = cle[i]


def get_term():
    return term
