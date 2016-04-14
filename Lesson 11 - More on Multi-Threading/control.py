"""
control.py: Creates queues, starts output and worker threads,
            and pushes inputs into the input queue.
"""
from queue import Queue
from output import OutThread
from worker import WorkerThread

WORKERS = 10

inq = Queue(maxsize = int(WORKERS * 1.5))
outq = Queue(maxsize = int(WORKERS * 1.5))

ot = OutThread(WORKERS, outq, sorting = False)
ot.start()

for i in range(WORKERS):
    w = WorkerThread(inq, outq)
    w.start()
instring = input("Words of wisdom: ")
for work in enumerate(instring):
    inq.put(work)
for i in range(WORKERS):
    inq.put(None)
inq.join()
print("Control thread terminating.")