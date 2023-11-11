import unittest
from lexeur import dictionnaire_ter as dictionnaire_ter


class MyTestCase(unittest.TestCase):
    def test_dictionnaire_ascii(self):
        term = dictionnaire_ter.term
        self.assertEqual(term.get('('), ord('('))
        self.assertEqual(term.get('7'), ord('7'))
        self.assertEqual(term.get('I'), ord('I'))
        self.assertEqual(term.get('elsif'), 260)
        self.assertEqual(term.get('procedure'), 274)
        self.assertEqual(term.get('num'), 286)


if __name__ == '__main__':
    unittest.main()