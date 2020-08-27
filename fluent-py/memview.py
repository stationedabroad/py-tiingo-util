from array import array

octets = array('B', range(100))
mem1 = memoryview(octets)

mem2 = mem1.cast('B', [5, 20])
print(mem2.tolist())

for i in range(20):
    mem2[1, i] = 100

print(f"cast one: {mem2.tolist()}")
mem3 = mem1.cast('B', [10, 10])

for n in mem3.tolist():
    print(n)


