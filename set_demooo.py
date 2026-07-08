# unordered data type

# you 'CANNOT' define empty set using literals
emptyset = set()

sampleset = {1,'A',3.86,'b',4,9,'reza','A','A','A'}

for _ in range(10):
  print(sampleset)


odd = set(range(1 ,50,2))   #members: 25
power = {1,4,9,16,25,36,49}  #members: 7


print(len(odd))
print(odd.intersection(power))
print(len(odd.union(power)))

print('=' *40)
print(odd.intersection_update(power))
print(odd)

power_frozen = frozenset(power)
power_frozen.