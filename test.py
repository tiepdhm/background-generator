import unittest
import main


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param1 = 10
        test_param2 = 5
        res = main.divide(test_param1, test_param2)
        self.assertEqual(res, 2)

    def test_do_stuff2(self):
        test_param1 = 9
        test_param2 = 0
        res = main.divide(test_param1, test_param2)
        self.assertIsInstance(res, ZeroDivisionError)

    def test_do_stuff3(self):
        test_param1 = None
        test_param2 = 5
        res = main.divide(test_param1, test_param2)
        self.assertEqual(res, 'please enter the numbers')

    def tearDown(self):
        print('clean up')


if __name__ == '__main__':
    unittest.main()
