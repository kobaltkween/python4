def trace(f):
    "Decorate a function to print a message before and after execution."
    def traced(*args, **kw):
        "Print message before and after a function call."
        print("Entering", f.__name__)
        result = f(*args, **kw)
        print("Leaving", f.__name__)
        return result
    return traced

def callable(o):
    return hasattr(o, "__call__")

def mtrace(cls):
    for key, val in cls.__dict__.items():
        if key.startswith("__") and key.endswith("__") \
                or not callable(val):
            continue
        setattr(cls, key, trace(val))
        print("Wrapped", key)
    return cls

@mtrace
class dull:
    def method1(self, arg):
        print("Method 1 called with arg", arg)
        
    def method2(self, arg):
        print("Method 2 called with arg", arg)
        
d = dull()
d.method1("Hello")
d.method2("Goodbye")

def framework(f):
    f.framework = True
    f.author = "Myself"
    return f

@framework
def somefunc(x):
    pass

print(somefunc.framework)
print(somefunc.author)

counts = {}
def countable(ftype):
    "Returns a decorator that counts each call of a function against ftype."
    def decorator(f):
        "Decorates a function and counts each call."
        def wrapper(*args, **kw):
            "Counts every call as being of the given type."
            try:
                counts[ftype] += 1
            except KeyError:
                counts[ftype] = 1
            return f(*args, **kw)
        return wrapper
    return decorator

@countable("short")
def f1(a, b = None):
    print("f1 called with", a, b)
    
@countable("f2")
def f2():
    print("f2 called")
    
@countable("short")
def f3(*args, **kw):
    print("f3 called", args, kw)
    
for i in range(10):
    f1(1)
    f2()
    f3(i, i*i, a = i)
    
for k in sorted (counts.keys()):
    print(k, ":", counts[k])