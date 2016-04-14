"""
Test list of list based array implementations using tuple subscripting.
"""
import unittest
import arr

class TestArray(unittest.TestCase):
    
    def testZeroes(self):
        for N in range(4):
            a = arr.array(N, N, N)
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        self.assertEqual(a[i, j, k], 0)
    
    def testIdentity(self):
        for N in range(4):
            a = arr.array(N, N, N)
            for i in range(N):
                a[i, i, i]  = 1
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        self.assertEqual(a[i, j, k], i == j == k)
                    
    def _index(self, a, r, c, z):
        return a[r, c, z]
    
    def testKeyValidity(self):
        a = arr.array(10, 10, 10)
        self.assertRaises(KeyError, self._index, a, -1, 1, 1)
        self.assertRaises(KeyError, self._index, a, 10, 1, 1)
        self.assertRaises(KeyError, self._index, a, 1, -1, 1)
        self.assertRaises(KeyError, self._index, a, 1, 10, 1)
        self.assertRaises(KeyError, self._index, a, 1, 1, 10)
        self.assertRaises(KeyError, self._index, a, 1, 1, -1)
        

if __name__ == "__main__":
    unittest.main()
                    