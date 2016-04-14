"""
Some tests of the Tree class
"""
import unittest
from mytree import Tree

class TestMyTree(unittest.TestCase):
    
    def setUp(self):
        self.t = Tree("V1", [1, "foo", 3])
        self.t.insert("U128", {"name" : "Malik Tawil"})
        self.t.insert("M1", 222)
        self.t.insert("A2", "M")
        self.t.insert("B4", {"foo" : "bar"})
        self.t.insert("C10", "this is a string")
    
    def testInsertExisting(self):
        self.assertRaises(ValueError, self.t.insert, "A2", "foobar")
        
    def testFind(self):
        self.assertEqual(self.t.find("M1"), 222)
        self.assertEqual(self.t.find("B4"), {"foo" : "bar"})
        self.assertEqual(self.t.find("C10"), "this is a string")
        self.assertEqual(self.t.find("V1"), [1, "foo", 3])
    
    def testFindFail(self):
        self.assertRaises(KeyError, self.t.find, "AK")
        
        
if __name__ == "__main__":
    unittest.main()