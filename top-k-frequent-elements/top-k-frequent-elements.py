from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # for mapping the occurences of the values
        freq = [[] for i in range(len(nums) + 1)] # this is where we are going to map the number of occurrences (by index) -> values
        tot = 0 # keep up with our k limit of values

        for num in nums: # for loop to initialize our dictionary
            count[num] = 1 + count.get(num, 0) 
        
        for num, key in count.items(): # for loop for mapping the occurences to values in our frequence multi-array
            freq[key].append(num) 


        ans = [] # our answer array
        for vals in range(len(freq) - 1, 0, -1): # we need to loop from the back to start from the max occurences
            for i in freq[vals]: # looping through the values in the array
                if tot < k: # checks our k limit
                    if len(freq[vals]) != 0: # if occurance list isn't empty
                        ans.append(i) # add a value to answer array
                        tot += 1 # increase our k amount
        return ans
