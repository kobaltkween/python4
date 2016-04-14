"""
mmapVSwrite.py:  Testing the speed of creating a 10 MB file using mmap against simply
                writing a file.
"""
import mmap
import os
from timeit import timeit

FN = "tempfile"
FS = 10 * 1024 * 1024  # 1MB = 1024 * 1024 bytes

def buildMmapFile(chunkSize):
    chunk = chunkSize * b"*"
    with open(FN, "w+b") as f:
        mapf = mmap.mmap(f.fileno(), FS, access = mmap.ACCESS_WRITE)
        fileSize = 0
        while fileSize < FS:
            mapf[fileSize : fileSize + chunkSize] = chunk
            fileSize += chunkSize
        mapf.close()
    os.unlink(FN)

def buildWriteFile(chunkSize):
    # 1MB = 2 ** 20 bytes
    chunk = chunkSize * b"*"
    with open(FN, "wb") as f:
        fileSize = 0
        while fileSize < FS:
            f.write(chunk)
            fileSize += chunkSize
        f.close()
    os.unlink(FN)

if __name__ == "__main__":
    chunks =  [2 ** i for i in range(2, 21)]
    print("{0}  {1:^8}  {2:^8}".format(" " * 10, "Mmap", "Write"))
    print("{0}  {1}  {2}".format("Chunk Size", "-" * 8, "-" * 8))
    for c in chunks:
        time1 = timeit("buildMmapFile(c)", setup = "from __main__ import buildMmapFile, FN, FS, c", number = 1)
        time2 = timeit("buildWriteFile(c)", setup = "from __main__ import buildWriteFile, FN, FS, c", number = 1)
        print("{0:>9}:  {1:>8}  {2:>8}".format(c, round(time1, 4), round(time2, 4)))
        