"""
thread.py: demonstrate creation and parallel execution of threads.
"""

import threading
import time

def run(i, name):
    """Sleep for a given number of seconds, report and terminate."""
    time.sleep(i)
    print(name, "finished after", i, "seconds")
    
for i in range(6):
    t = threading.Thread(target = run, args = (i, "T" + str(i)))
    t.start()
    
print("Threads started")