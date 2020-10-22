import unittest

from main import findLCA, root


class TestLCA(unittest.TestCase):
    def testLCA(self):
        self.assertEqual((findLCA(root, 4, 5)), 2, "should be equal to 2")
        self.assertEqual((findLCA(root, 4, 6)), 1, "should be equal to 1")
        self.assertEqual((findLCA(root, 3, 4)), 1, "should be equal to 1")
        self.assertEqual((findLCA(root, 2, 4)), 2, "should be equal to 2")


if __name__ == '__main__':
    unittest.main()
    print("All tests have passed")
