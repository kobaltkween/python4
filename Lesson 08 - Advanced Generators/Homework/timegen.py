from random import random
from timeit import timeit

num = 1000000
tries = 10
        
def mkgen(n):
    for i in range(n):
        yield random()

print("Testing list of", num, "random numbers")
print("List comprehension:", timeit("[random() for i in range(num)]", setup = "from __main__ import num, random", number = tries))
print("List function:", timeit("list(random() for i in range(num))", setup = "from __main__ import num, random", number = tries))

print("Testing generator of", num, "random numbers")
print("List comprehension:", timeit("[i for i in mkgen(num)]", setup = "from __main__ import num, mkgen, random", number = tries))
print("List function:", timeit("list(i for i in mkgen(num))", setup = "from __main__ import num, mkgen, random", number = tries))
