from array import array
octets = array('B', range(100))
mem1 = memoryview(octets)

mem2 = mem1.cast('B', [5, 20])
print(mem2.tolist())

mem2[1,1] = 100
mem2[1,2] = 100
print(mem2.tolist())
