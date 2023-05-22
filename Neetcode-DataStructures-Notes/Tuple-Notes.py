# Tuples are like arrays but are immutable
tup = (1, 2, 3)
print(tup)
print(tuple[0])
print(tuple[-1])

# can't modify

# tup[0] = 2 won't work

# mainly use tuples as key for hash map/set
myMap = {(1,2): 3}
print(myMap[(1,2)])

mySet = set()
mySet.add((1,2))
print((1,2) in mySet)

#Lists are not hashable so they cannot be keys
# myMap[[3,4]] = 5 won't work 