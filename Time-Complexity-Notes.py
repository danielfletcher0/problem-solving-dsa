#Definition for Time Complexity
#How many iterations / operations does the algo do in regards to n

#O(1) Constant Time Complexity example

def dummy_function(nums): #input size: n = len(nums)
    #How many operations does the algo do in regards to n?
    sum = 0
    return sum

    # O(2) due to sum and return being a constant operation
    # O(2) => O(1) => constant time complexity
    # The runtime is the same (constant) no matter the size of the input
    # n = 3 => 1
    # n = 10 => 1
    # n = 1000 => 1

'''
Constant time is better (faster) than linear time =>  O(1) < O(n)

Task: Given an integer n, write a function that returns 1 + 2 + 3 + ... + n
'''

def brute_force(n):
    sum = 0 # 1
    for i in range(1, n + 1): # n iterations
        sum+= i # 1
    return sum # 1

# 1 + n * 1 + 1 => O(n + 2) => O(n) => linear time complexity


def gausss_sum(n): # 1 + 2 + 3 + ... + n = n * (n + 1) / 2
    return n * (n + 1) / 2 # 1 (addition) + 1 (multiplication) + 1 (division) + 1 (return) = O(4) => O(1) => constant time complexity



#Built in functions time complexity


def sum(nums): # O(n)
    list_sum = 0
    for i in range(len(nums)): # n iterations
        list_sum += nums[i]
    return list_sum

def get_sum(nums): # O(n)
    return sum(nums) # O(n)

#---------------------------------------
def max(nums): # O(n)
    max_val = nums[0] # O(1)
    for i in range(1, len(nums)): # n - 1 iterations
        if nums[i] > max_val: # O(1)
            max_val = nums[i] # O(1)
    return max_val # O(1)

# 1 + (n - 1) * (2 + 1) + 1 = 3 * (n - 1) + 2 = O(3n - 1) => O(n)

def get_max(nums): # O(n) overall
    return max(nums) # O(n)

#----------------------------------------

def min(nums): # O(n)
    min_val = nums[0] # O(1)
    for i in range(1, len(nums)): # n - 1 iterations
        if nums[i] < min_val: # O(1)
            min_val = nums[i] # O(1)
    return min_val # O(1)


def get_min(nums): # O(n) overall
    return min(nums) # O(n)

#------------------------------------------

def find_num(nums, num): #O(n)
    for value in nums: # O(n) worst case scenario
        if value == num: # O(1)
            return True # O(1)
    return False # O(1)

def find_num(nums, num):
    
    return num in nums #------^ 