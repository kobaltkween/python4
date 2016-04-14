"""
control.py: Creates queues, starts output and worker processes,
            and pushes inputs into the input queue.
"""
from multiprocessing import Queue, JoinableQueue
from output import OutThread
from worker import WorkerThread
from timeit import timeit
import string
import random

def process(n):
    WORKERS = 10
    inq = JoinableQueue(maxsize = int(WORKERS * 1.5))
    outq = Queue(maxsize = int(WORKERS * 1.5))
    
    ot = OutThread(WORKERS, outq, sorting = True)
    ot.start()
    
    for i in range(WORKERS):
        w = WorkerThread(inq, outq)
        w.start()
    
    instring = "".join(random.choice(string.ascii_letters) for i in range(n))

    for work in enumerate(instring):
        inq.put(work)
    for i in range(WORKERS):
        inq.put(None)
    inq.join()
    print("Control process terminating.")

if __name__ == "__main__":
    print("Processing took about", timeit("process(1000)", setup = "from __main__ import process", number = 1), "seconds.")