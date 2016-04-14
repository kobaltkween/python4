"""
Class-based dict allowing tuple subscripting and sparse data.
"""

class array:
    
    def __init__(self, M, N, Z):
        "Create a list long enough to hold M * N elements."
        self._data = {}
        self._rows = M
        self._cols = N
        self._zeds = Z
            
    def __getitem__(self, key):
        "Returns the appropriate element for a two-element subscript tuple."
        row, col, zed = self._validate_key(key)
        try:
            return self._data[row, col, zed]
        except KeyError:
            return 0
    
    def __setitem__(self, key, value):
        "Sets the appropriate element for a two-element subscript tuple."
        row, col, zed = self._validate_key(key)
        self._data[row, col, zed] = value
    
    def _validate_key(self, key):
        """
        Validates a key against the array's shape, returning good tuples.
        Raises Key Error on problems.
        """
        row, col, zed = key
        if (0 <= row < self._rows and 
            0 <= col < self._cols and
            0 <= zed < self._zeds):
            return key
        raise KeyError("Subscript out of range")