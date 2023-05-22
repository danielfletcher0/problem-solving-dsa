#HashMap (aka dict)

myMap = {}
myMap["alice"] = 88
myMap["bob"] = 77
print(myMap)
print(len(myMap)) #gives us the amount of keys

myMap["alice"] = 80 #maps are mutable
print(myMap)

print("alice" in myMap) #constant time
myMap.pop("alice") #removing the key also removes the value
print("alice" in myMap)

myMap = { "alice": 90, "bob": 70 }  #key on the left, value on the right
print(myMap)
#the same as manually inserting values into the hashmap

#Dict comprehension
myMap = {i: 2*i for i in range(3)}
print(myMap)

#Looping through maps
myMap = { "alice": 90, "bob": 70 }

for key in myMap:
    print(key, myMap[key])

for val in myMap.values():
    print(val)

for key, val in myMap.items():
    print(key, val)