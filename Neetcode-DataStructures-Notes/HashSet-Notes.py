#HashSet

mySet = set() #immutable and holds distinct values

mySet.add(1) # constant time operation
mySet.add(2)
print(mySet)
print(len(mySet))

#Can search a hashset without a function
print(1 in mySet)
print(2 in mySet)
print(3 in mySet)

mySet.remove(2) # can remove values in constant time
print(2 in mySet)

#list to set
print(set([1, 2, 3, 4]))

# Set comprehension
mySet = {i for i in range(1, 6)}
print(mySet)