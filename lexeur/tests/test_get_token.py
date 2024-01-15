import unittest

import lexeur.file_to_code_ter as file


class MyTestCase(unittest.TestCase):
    def test_dictionnaire_ascii(self):
        print("On commence par voir si notre lexeur reconnait bien l'entête d'un fichier Ada : ")
        self.assertEqual(file.get_token("../exemples/intro.ada"),
                         [284, (285, 'Ada'), 46, (285, 'Text_IO'), 59, 282, (285, 'Ada'), 46, (285, 'Text_IO'), 59])
        print(
            "On vérifie maintenant si notre lexeur reconnait bien les mots clés qui sont utilisés pour déclarer une "
            "procédure dans notre cas : ")
        self.assertEqual(file.get_token("../exemples/exemple_procedure.ada"),
                         [274, (285, 'Hello'), 267, 258, 261, (285, 'Hello'), 59])
        print(
            "On fait un dernier test sur une autre structure du langage : une bouble while contenant des variables, "
            "des mots clés et des affectations : ")
        self.assertEqual(file.get_token("../exemples/exemple_while.ada"),
                         [283, (285, 'Next'), 47, 61, (285, 'Head'), 268, (285, 'Sum'), 58, 61, (285, 'Sum'), 43,
                          (285, 'Next'), 46, (285, 'Value'), 59, (285, 'Next'), 58, 61, (285, 'Next'), 46,
                          (285, 'Succ'), 59, 261, 268, (285, 'Summation'), 59])


if __name__ == '__main__':
    unittest.main()
