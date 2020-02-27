import unittest


from homework import Fibonacci, Even, Factorials


class HomeworkTest(unittest.TestCase):

    def test_Fibonacci(self):
        obj = list(Fibonacci(5))
        self.assertEqual(obj, [0, 1, 1, 2, 3, 5])
        obj = list(Fibonacci(10))
        self.assertEqual(obj, [0, 1, 1, 2, 3, 5, 8])

    def test_Even(self):
        obj = list(Even(9))
        self.assertEqual(obj, [0, 2, 4, 6, 8])
        obj = list(Even(10))
        self.assertEqual(obj, [0, 2, 4, 6, 8, 10])

    def test_Factorials(self):
        obj = list(Factorials(4))
        self.assertEqual(obj, [1, 2, 6, 24])
        obj = list(Factorials(6))
        self.assertEqual(obj, [1, 2, 6, 24, 120, 720])


if __name__ == '__main__':
    unittest.main()
