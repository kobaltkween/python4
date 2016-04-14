"""
A subclass to dict that demonstrates how exceptions can be handled
"""
class MyDict(dict):
    def __init__(self, val):
        self.default = val
        
    def __getitem__(self, key):
        try:
            v = dict.__getitem__(self, key)
        except KeyError:
            v = self.default
        return v
    
if __name__ == "__main__":
    foo = MyDict("Key not found")
    foo["bar"] = 10
    print(foo["bar"])
    print(foo["boo"])
    