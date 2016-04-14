"""
A program testing current directory for three sequentially created threads.
"""
import threading
from os import chdir, getcwd
from random import random
import time

class DirThread(threading.Thread):
    def __init__(self, sleeptime, *args, **kw):
        threading.Thread.__init__(self, *args, **kw)
        self.sleeptime = sleeptime
        self.dir = getcwd()
        
    def run(self):
        for i in range(self.sleeptime):
            total = 0.0
            for j in range(2000000):
                total += 1 / (j * random() + 1)
            print(self.name, "finished pass", i)
        print(self.name, "finished")
        
    def changeDir(self):
        chdir("../")
        
    def getDir(self):
        print (self.name, "directory is", getcwd())
        
tt = [DirThread(i + 1) for i in range(3)]

for t in tt:
    t.start()
    t.getDir()
    
time.sleep(2)
tt[1].changeDir()

for t in tt:
    t.getDir()
"Just because I'm curious..."
for t in threading.enumerate():
    print(t.name)
    
"""
Initial testing seems to show that the current working directory is singular, 
and not thread dependent.  Which makes sense. Poking around online, there's 
only one working directory per process, so this would need to use
multi-processing to work in multiple directories concurrently.
"""
