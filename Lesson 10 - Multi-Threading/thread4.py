"""
thread.py: Use threading.Thread subclass to specify thread logic in run() method
"""

import threading
import time

class MyThread(threading.Thread):
    def __init__(self, sleeptime, *args, **kw):
        threading.Thread.__init__(self, *args, **kw)
        self.sleeptime = sleeptime
    
    def run(self):
        for i in range(self.sleeptime):
            for j in range(500000):
                k = j * j
            print(self.name, "finished pass", i)
        print(self.name, "finished after", self.sleeptime, "seconds")
   
bgthreads = threading.active_count()
tt = [MyThread(i + 3) for i in range(6)]

for t in tt:
    t.start()

print("Threads started")

while threading.active_count() > bgthreads:
    time.sleep(2)
    print("tick")
print("All threads done")