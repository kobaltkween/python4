from contextlib import contextmanager

@contextmanager
def ctxman():
    try:
        cm = object()
        yield cm
        print("With concluded normally")
    except Exception as e:
        if type(e)!= ValueError:
            raise
        
if __name__ == "__main__":
    # Make sure it works properly when there's no exception
    with ctxman() as cm:
        print("ID(cm):", id(cm))
        
    # Make sure it works properly when there's a non-ValueError exception
    try: 
        with ctxman() as cm:
            1/0
    except Exception as e:
        print(type(e).__name__, "raised.")
    
    # Make sure it works properly when there's a ValueError exception    
    try:
        with ctxman() as cm:
            int("foo")
        print("No exception raised.")
    except Exception as e:
        print("Context manager raised an exception.")