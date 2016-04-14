"""
Using introspection to list the names and arguments of functions in a module.
"""
import inspect
import os

for f in inspect.getmembers(os, inspect.isfunction):
    print("def", f[0], inspect.formatargspec(*inspect.getfullargspec(getattr(os, f[0]))))
