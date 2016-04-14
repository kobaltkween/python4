from contextlib import contextmanager

@contextmanager
def ctxman(raising = False):
    try:
        cm = object()
        print("Context manager returns:", id(cm))
        yield cm
        print("With concluded normally")
    except Exception as e:
        print("Exception", e, "raised")
        if raising:
            print("Re-raising exception")
            raise
    