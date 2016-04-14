"""
Test for a addarg.py, a simple decorator function exercise.
"""
import unittest
from addarg import addarg

class TestAddArg(unittest.TestCase):
    
    def testArgs(self):
        @addarg(1)
        def prargs(*args):
            return args
        self.assertEqual(prargs(2, 3), (1, 2, 3))
        self.assertEqual(prargs("child"), (1, "child"))
    
    def testKwargs(self):
        @addarg("decorated!")
        def tkwargs(*args, **kwargs):
            return args, kwargs
        self.assertEqual(tkwargs(name = "John", age = 23), (("decorated!",), {"name" : "John", "age" : 23}))
        self.assertEqual(tkwargs(food = "bread"), (("decorated!",), {"food" : "bread"}))

        
    
if __name__ == "__main__":
    unittest.main()