"""
control.py: Creates queues, starts output and worker threads,
            and pushes inputs into the input queue.
"""
from queue import Queue
from output import OutThread
from worker import WorkerThread
from timeit import timeit
import string
import random

def process():
    WORKERS = 10
    letters = 1000
    inq = Queue(maxsize = int(WORKERS * 1.5))
    outq = Queue(maxsize = int(WORKERS * 1.5))
    
    ot = OutThread(WORKERS, outq, sorting = False)
    ot.start()
    
    for i in range(WORKERS):
        w = WorkerThread(inq, outq)
        w.start()
    
    instring = "".join(random.choice(string.ascii_letters) for i in range(letters))

    for work in enumerate(instring):
        inq.put(work)
    for i in range(WORKERS):
        inq.put(None)
    inq.join()
    print("Control thread terminating.")

print("Processing took about", timeit("process()", setup = "from __main__ import process", number = 1), "seconds.")