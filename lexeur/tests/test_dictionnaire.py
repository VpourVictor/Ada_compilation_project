import unittest
import lexeur.dictionnaire_ter as dictionnaire_ter


class MyTestCase(unittest.TestCase):
    def test_dictionnaire_ascii(self):
        term = dictionnaire_ter.term
        print("On vérifie que les caractères sont bien associés à leur valeur ascii")
        print("Exemple pour un symbole :")
        self.assertEqual(term.get('('), ord('('))
        print("Exemple pour un chiffre :")
        self.assertEqual(term.get('7'), ord('7'))
        print("Exemple pour une lettre :")
        self.assertEqual(term.get('I'), ord('I'))
        print("Exemple pour un mot clé :")
        self.assertEqual(term.get('elsif'), 260)
        self.assertEqual(term.get('procedure'), 274)
        print("Exemple pour un num : ")
        self.assertEqual(term.get('num'), 286)
        print("Exemple pour un ident : ")
        self.assertEqual(term.get('id'), 285)
        print("Les exemples montrent bien que l'association dans le dictionnaire est correcte")

if __name__ == '__main__':
    unittest.main()