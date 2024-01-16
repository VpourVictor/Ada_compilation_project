import unittest
import lexeur.file_to_code_ter as file


class MyTestCase(unittest.TestCase):
    def test_token_list(self):
        #
        token_list_test = []
        token_list_true = [51]
        print("La fonction treat_a_string retourne le token associé à la valeur passée en premier paramètre")
        self.assertEqual(file.treat_a_string("3", token_list_test), token_list_true)
        token_list_true.append(274)
        self.assertEqual(file.treat_a_string("procedure", token_list_test), token_list_true)
        token_list_true.append((285, "Ada"))
        self.assertEqual(file.treat_a_string("Ada", token_list_test), token_list_true)
        token_list_true.append((286, "32309"))
        self.assertEqual(file.treat_a_string("32309", token_list_test), token_list_true)
        print("On voit bien que les 2 lists sont identiques")
        print("Avec les entiers qui se voient attribuer leur valeur en ascii")
        print("Les mots clés se voient attribuer leur code dans le dictionnaire")
        print("Les chaines de caractères se voient attribuer le code 285 -> ident et sont associées à leur valeur")
        print("Les nombres se voient attribuer le code 286 -> num et sont associés à leur valeur")
        print(token_list_test)
        print(token_list_true)

        print("Les tests qui suivent visent à montrer que même si on colle les opérateurs, "
              "la fonction fait bien la distinction et traitre chaque caractère comme un token à part entière")
        token_list_test = []
        token_list_true = [53, 43, 51]
        self.assertEqual(file.treat_a_string("5+3", token_list_test), token_list_true)

        token_list_test = []
        token_list_true = [53, 43, 51, 42, 53]
        self.assertEqual(file.treat_a_string("5+3*5", token_list_test), token_list_true)

        token_list_test = []
        token_list_true = [53, 43, 51, 42, 53, 47, 53]
        self.assertEqual(file.treat_a_string("5+3*5/5", token_list_test), token_list_true)


if __name__ == '__main__':
    unittest.main()
