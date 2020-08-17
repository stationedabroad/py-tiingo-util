from array import array
octets = array('B', range(100))
mem1 = memoryview(octets)
print(mem1.tolist())
