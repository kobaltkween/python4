"""
Small test for dictex.py
"""
import unittest
from dictex import MyDict

class TestDictTex(unittest.TestCase):
        
    def testMyDict(self):
        default = "No key found."
        d = MyDict(default)
        d["foo"] = "bar"
        d["ten"] = 10
        self.assertEqual(d["foo"], "bar")
        self.assertEqual(d["ten"], 10)
        self.assertEqual(d["kay"], default)
        self.assertEqual(d[234], default)
        
if __name__ == "__main__":
    unittest.main()