import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        # result = calc.add(1,3)
        # self.assertEqual(result, 4)

        self.assertEqual(calc.add(1,2),3)
        self.assertEqual(calc.add(-1,1),0)
        self.assertEqual(calc.add(-1,-2),-3)


    def test_sub(self):
        self.assertEqual(calc.subtract(3,2),1)
        self.assertEqual(calc.subtract(1,1),0)
        self.assertEqual(calc.subtract(-1,-1),0)

    def test_mul(self):
        self.assertEqual(calc.multiply(3, 2), 6)
        self.assertEqual(calc.multiply(1, 1), 1)
        self.assertEqual(calc.multiply(1,0),0)
        self.assertEqual(calc.multiply(-1,-1), 1)

    def test_div(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1,-1),1)
        # self.assertRaises(ValueError,calc.divide,10,0)

        #We can also do it using context manager
        with self.assertRaises(ValueError):
            calc.divide(10,0)
# TO RUN DIRECTLY
if __name__ == "__main__":
    unittest.main()