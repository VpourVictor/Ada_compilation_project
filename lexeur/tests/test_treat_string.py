import unittest
import lexeur.file_to_code_ter as file


class MyTestCase(unittest.TestCase):
    def test_token_list(self):
        token_list_test = []
        token_list_true = [51]
        self.assertEqual(file.treat_a_string("3", token_list_test), token_list_true)
        token_list_true.append(274)
        self.assertEqual(file.treat_a_string("procedure", token_list_test), token_list_true)
        token_list_true.append((285, "Ada"))
        self.assertEqual(file.treat_a_string("Ada", token_list_test), token_list_true)
        token_list_true.append((286, "32309"))
        self.assertEqual(file.treat_a_string("32309", token_list_test), token_list_true)


if __name__ == '__main__':
    unittest.main()
