"""
output.py: The output process for miniature framework.
"""

identity = lambda x: x

from multiprocessing import Process
import sys

class OutThread(Process):
    def __init__(self, N, q, sorting = True, *args, **kw):
        """Initialize process and save queue reference."""
        Process.__init__(self, *args, **kw)
        self.queue = q
        self.workers = N
        self.sorting = sorting
        self.output = []
        
    def run(self):
        """Extract items from the output queue aqnd print until all done."""
        while self.workers:
            p = self.queue.get()
            if p is None:
                self.workers -= 1
            else:
                # this is a real output packet
                self.output.append(p)
        print(len("".join(c for (i, c) in (sorted if self.sorting else identity)(self.output))))
        print("Output process terminating")
        sys.stdout.flush()