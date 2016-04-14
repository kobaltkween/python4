"""
testComposable.py: performs simple tests of composable functions.
"""
import unittest
from composable import Composable

def reverse(s):
    "Reverses a string using negative-stride sequencing"
    return s[::-1]

def square(x):
    "Multiplies a number by itself."
    return x * x

class ComposableTestCase(unittest.TestCase):
    
    def testInverse(self):
        reverser = Composable(reverse)
        nulltran = reverser * reverser
        flipped = reverser ** 5
        testSet = ("", "a", "0123456789", "abcdefghijklmnopqrstuvwxyz")
        for s in testSet:
            self.assertEqual(nulltran(s), s)
        for s in testSet:
            self.assertEqual(flipped(s), reverse(s))
        
    
    def testSquare(self):
        squarer = Composable(square)
        po4 = squarer * square
        for v, r in ((1, 1), (2, 16), (3, 81)):
            self.assertEqual(po4(v), r)
        po16 = squarer ** 4
        for v, r in ((1, 1), (2, 65536), (3, 43046721)):
            self.assertEqual(po16(v), r)
    
    def testExceptions(self):
        fc = Composable(square)
        with self.assertRaises(TypeError):
            fc = fc * 3
        with self.assertRaises(TypeError):
            fc = square * fc
        with self.assertRaises(TypeError):
            fc = fc ** "16"
        with self.assertRaises(ValueError):
            fc = fc ** -2
            
    def testType(self):
        fc = Composable(square)
        fc = fc ** 1
        self.assertTrue(type(fc) == Composable)
            
    
if __name__ == "__main__":
    unittest.main()