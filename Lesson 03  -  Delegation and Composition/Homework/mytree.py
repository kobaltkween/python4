"""
Simple recursive structure exercise.
"""

class Tree:
    def __init__(self, key, value):
        "Create a new Tree object with empty L & R subtrees."
        self.key = key
        self.value = value
        self.left = self.right = None
    
    def insert (self, key, value):
        "Insert a new element into the tree in the correct position."
        if key < self.key:
            if self.left:
                self.left.insert(key, value)
            else:
                self.left = Tree(key, value)
        elif key > self.key:
            if self.right:
                self.right.insert(key, value)
            else:
                self.right = Tree(key, value)
        else:
            raise ValueError("Attempt to insert duplicate value.")
    
    def walk(self):
        "Generate the keys from the tree in sorted order."
        if self.left:
            for n in self.left.walk():
                yield n
        yield self.key, self.value
        if self.right:
            for n in self.right.walk():
                yield n
                
    def find(self, key):
        "Look for a key in the tree, and return its value if found."
        if self.key  == key:
            return self.value
        if self.left:
            for n in self.left.walk():
                if n[0] == key:
                    return n[1]
        if self.right:
            for n in self.right.walk():
                if n[0] == key:
                    return n[1]
        raise KeyError("Key {} not found in Tree".format(key))
    
if __name__ == "__main__":
    t = Tree("D", 4)
    for c in "BJQKFAC":
        t.insert(c, ord(c))
    
    print(list(t.walk()))
    print(t.key)
    print(t.find("K"))
    print(t.find("D"))
    t.find("k")    