import unittest
import lexeur.file_to_code_ter as file
import parseur.functions


class MyTestCase(unittest.TestCase):
    def test_functions(self):
        token_list = [284, (285, 'Ada'), 46, (285, 'Text_IO'), 59]
        self.assertTrue(parseur.functions.fonction_N1(token_list))


if __name__ == '__main__':
    unittest.main()
