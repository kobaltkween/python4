with open("hello.txt", "wb") as f:
    f.write(b"Hello Python!\n")

import mmap
with open("hello.txt", "r+b") as f:
    mapf = mmap.mmap(f.fileno(), 36, access = mmap.ACCESS_WRITE)
    print(mapf.readline()) # prints b"Hello Python!\n"
    print(mapf[:5]) # prints b"Hello"
    print(mapf.tell())
    print(len("Hello Python!\n"))
    print(len("Hello world!\n"))
    mapf[14:27] = b"Hello world!\n"
    mapf.seek(0)
    print(mapf.readline()) # prints b"Hello  world!\n"
    mapf.close()
    
with open("test.txt", "w+b") as f:
    mapf = mmap.mmap(f.fileno(), 30, access = mmap.ACCESS_WRITE)
    mapf[0:10] = b"*"*10
    mapf[10:20] = b"-"*10
    mapf[20:30] = b"*"*10
    print(mapf.readline())
    mapf.close()