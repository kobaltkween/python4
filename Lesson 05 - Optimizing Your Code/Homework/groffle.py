"""
Program for optimization.  Python 4, Lesson 5.

Calculates the groffle speed of a knurl widget
of average density given by user input.
"""

from math import log
from timeit import Timer

def process(n):
    return 1/n

def groffleSlow(mass, density):
    total = 0.0
    for i in range(10000):
        masslog = log(mass * density)
        total += masslog / (i + 1)
    return total

def groffleFast(mass, density): 
    total = 0.0 
    masslog = log(mass * density) 
    for i in range(1, 10001): 
        total += 1 / i
    return masslog * total

mass = 2.5
density = 12.0 
timer1 = Timer("total = groffleSlow(mass, density)", 
 "from __main__ import groffleSlow, mass, density")
timer2 = Timer("total = groffleFast(2.5, 12.0)", 
 "from __main__ import groffleFast") 

print("Original time:", timer1.timeit(number = 1000))
print("Optimized time:", timer2.timeit(number = 1000))

groffleFR = groffleFast(mass, density)
groffleSR = groffleSlow(mass, density)
def floatCompare(a, b, tol):
    """
    Specialized comparison for floats since they can't be expressed or managed precisely in binary.
    """
    if abs(a - b) < tol:
        return True
    
if floatCompare(groffleFR, groffleSR, 0.0000001):
    print("The results of the two functions are the same.")
else:
    print("The functions get different results.  Fix it.")
    print("Original result:", groffleSR)
    print("New result:", groffleFR)

"""
Base time: 4.0595
Change 1 - move masslog out of loop: positive - 2.2133
Change 2 - eliminate mass and density variables in function: neutral - 2.1802
Change 3 - eliminate variables, but pass the numbers as arguments: neutral - 2.1895
Change 4 - Take masslog variable out of loop: positive - 1.5724
Change 5 - Change range, make loop addition unnecessary: positive - 1.0900
Change 6 - Use lambda and map instead of for loop: negative - 1.8268
"""