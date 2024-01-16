import unittest
from parseur.compare import compare_string, compare


class MyTestCase(unittest.TestCase):
    def test_compare_string(self):
        # test compare string
        self.assertEqual(True, compare_string("chat", "chats"))
        self.assertEqual(True, compare_string("python", "pysthon"))
        self.assertEqual(False, compare_string("abc", "xyz"))
        self.assertEqual(False, compare_string("hello", "holla"))
        self.assertEqual(False, compare_string("hello", "holl"))
        self.assertEqual(False, compare_string("hello", "holl2"))
        self.assertEqual(True, compare_string("123", "423"))
        self.assertEqual(True, compare_string("chat", "caht"))
        self.assertEqual(True, compare_string("hello", "hllo"))
        self.assertEqual(False, compare_string("chat", "ctah"))
        self.assertEqual(True, compare_string("chat", "hat"))
        self.assertEqual(True, compare_string("chat", "cha"))

    def test_compare(self):
        # test compare
        self.assertEqual(True, compare(65, 65))

        self.assertEqual(True, compare(283, (285, "whole")))
        self.assertEqual(True, compare((285, "whOle"), 283))

        self.assertEqual(True, compare(283, (285, "hile")))
        self.assertEqual(True, compare(283, (285, "whisle")))
        self.assertEqual(True, compare(283, (285, "whiles")))
        self.assertEqual(True, compare(283, (285, "whle")))
        self.assertEqual(True, compare(283, (285, "whlle")))
        self.assertEqual(True, compare(283, (285, "ehile")))
        self.assertEqual(True, compare(283, (285, "whlie")))

        self.assertEqual(False, compare((285, "whisle"), 65))

        self.assertEqual(False, compare((286, "125"), (285, "12y")))
        self.assertEqual(True, compare((285, "12y"), (286, "125")))


if __name__ == '__main__':
    unittest.main()
