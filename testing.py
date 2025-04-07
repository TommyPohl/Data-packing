import unittest


def add(a, b):
    return a + b


class TestMath(unittest.TestCase):
    def test_add_int(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_float(self):
        self.assertEqual(add(2.5, 3.5), 6)
        
    def test_add_neg(self):
        self.assertEqual(add(-2.5, 2.5), 0)
        self.assertEqual(add(-2.5, -2.5), -5)
        self.assertEqual(add(2.5, -2.5), 0)




if __name__ == '__main__':
    unittest.main() 
2