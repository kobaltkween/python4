"""
thread.py: demonstrate thread monitoring by awaiting termination.
"""

import threading
import time

def run(i, name):
    """Sleep for a given number of seconds, report and terminate."""
    time.sleep(i)
    print(name, "finished after", i, "seconds")

threads = []
   
for i in range(6):
    t = threading.Thread(target = run, args = (i, "Thread-" + str(i)))
    t.start()
    threads.append((i, t))
    
print("Threads started")
for i, t in threads:
    t.join()
    print("Thread", i, "done")
    
print("All threads done")