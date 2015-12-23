import time
from array_list import ArrayList

n = 100000

L = []
start = time.clock()
for i in range(n): L.append(i)
stop = time.clock()
print("Python list, append %d items: %.5f" % (n,(stop-start)))

L = ArrayList(dtype=int)
start = time.clock()
for i in range(n): L.append(i)
stop = time.clock()
print("Array list, append %d items: %.5f" % (n,(stop-start)))

L = ArrayList(dtype=int)
start = time.clock()
L.append(range(n), 1)
stop = time.clock()
print("Array list, append %d items at once: %.5f" % (n,(stop-start)))


L = []
start = time.clock()
for i in range(n): L.insert(0,i)
stop = time.clock()
print("Python list, prepend %d items: %.5f" % (n,(stop-start)))

L = ArrayList(dtype=int)
start = time.clock()
for i in range(n): L.insert(0,i)
stop = time.clock()
print("Array list, prepend %d items: %.5f" % (n,(stop-start)))

L = ArrayList(dtype=int)
start = time.clock()
L.append(range(n,0,-1), 1)
stop = time.clock()
print("Array list, append %d items at once: %.5f" % (n,(stop-start)))
