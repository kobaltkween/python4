class ctxmgr:
    def __init__(self, raising = True):
        print("Created new context manager object", id(self))
        self.raising = raising
    
    def __enter__(self):
        print("__enter__ called")
        cm = object()
        print("__enter__ return object id:", id(cm))
        return cm
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__ called")
        if exc_type:
            print("An exception occurred.")
            if self.raising:
                print("Re-raising exception")
            return not self.raising
        