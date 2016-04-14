"""
addarg: An exercise in decorator functions.
"""

def addarg(arg):
    "Outer function that takes arguments."
    def deco(f):
        "Standard decorator that takes in functions"
        def wrap(*args, **kwargs):
            "Adds argument to function calls"
            return f(arg, *args, **kwargs)
        return wrap
    return deco

if __name__ == "__main__":
    @addarg(1)
    def prargs(*args):
        return args
    print(prargs(2, 3))
    print(prargs("child"))