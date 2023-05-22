import math
"These are going to be all the notes for the in and outs you need for python for when studying Data Structures and Algorithms"

#python is a dynamically typed variable, meaning after initialize a variable you can reassign it to any other type

#For example
int_variable = 0 #<- We assign this int_variable with an integer value of 0
int_variable = "0" #<- Now we've reassigned it to hold a string value

#Python also allows multiple assignments, if we have two variables we put them on the left side then are equal sign then the corresponding values on the right side

int_a , int_b = 0, 1

#Null in python is classifed with the None value, can also be reassigned
null_value = None
null_value = "abc"

#if statments don't need paranthesis, and also don't need curly braces to represent the body statements. We use indentation. Else if is "elif"
#and = &&
#or = ||

n = 1
if (n > 0) and (n < 2):
    n-=1

#Useful math helpers
print(math.floor(3/2)) # <-rounds integer down the result after doing the calculation
print(math.ceil(3/2)) #<- rounds integer up the result after doing the calculation
print(math.sqrt(2)) #<- returns the square root of the passed in value
print(math.pow(3,2)) #<- returns the value of 3 raised to the 2nd power

#How python represents infinity values
float("inf") #<- represents positive infinity
math.inf #also represents positive infinity as well
float("-inf") #<- represents negative infinty
-math.inf #represents negative infinty as well

#Arrays (called lists in python) ONE OF THE MOST IMPORTANT DATA STRUCTURES BESIDES HASHMAPS

arr = [1,2,3]
print(arr)

#can be used as a stack
arr.append(4) #adds value on top of the stack
arr.append(5)
print(arr)

arr.pop() #pops off the last value from the top of the stack
print(arr)

arr.insert(1,7) #can insert values into the middle of the array O(n)
print(arr)

arr[0] = 0 #is not O(n)
arr[3] = 0 #these operations are constant time

n = 5

#to initialize an array of n size
arr = [1] * n
print(arr)
print(len(arr))

#Sublists  (aka slicing)
arr = [1,2,3,4]
print(arr[1:3]) #similar to for loops, first index is included, second index is excluded
print(arr[0:4]) #returns all the elements
print(arr[:]) #returns all elements as well
print(arr[::-1]) #returns all elements in reverse

#Unpacking
#assigns the variable with each element in the array
#super helpful for going through the lists of pairs
#be careful because you have to make sure the number of variables match the number of elements
a, b, c = [1, 2, 3]  
print(a,b,c)

#Loop through arrays

nums = [1, 2, 3]

#Using index
for i in range(len(nums)):
    print(nums[i])

#Without using index

for value in nums:
    print(value)

#If you need both the index and the value, use enumerate

for index, value in enumerate(nums):
    print(index, value, sep=" ")

# Loop through multiple arrays simultaneously
# with unpacking

nums1 = [1, 3, 5]
nums2 = [2, 4, 6]

for n1, n2 in zip(nums1, nums2):
    print(n1, n2)

#reversing an array
nums = [1, 2, 3]
nums.reverse()
print(nums)

#Sorting

arr = [5, 2, 6, 4, 7]
print(arr)
arr.sort() #sorts in ascending order by default
print(arr)

arr.sort(reverse=True) #to sort in descending order

arr = ["a", "t", "b"] #we can also sort a list of strings
arr.sort() #by default it is sorted by alphabet

#Custom sort (by length of string)

arr.sort(key=lambda x: len(x))

#List comprehension
arr = [i for i in range(5)] #creates a list with the values in the range of 5

# 2-D lists

arr = [[0] * 4 for i in range(4)]

print(arr)

# for finding the ascii value of a char

print(ord('a'))
print(ord('b'))

#combining list of strings (with an empty string delimeter)

strings = ["ab", "cd", "ef"]

print("".join(strings))

