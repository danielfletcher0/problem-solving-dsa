class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        if 1 not in nums:
            return 1
        for data in range(n):
            if nums[data] > n or nums[data] <= 0:
                nums[data] = 1
            
        for i in range(n):
            a = abs(nums[i])
            if a == n:
                nums[0] = - abs(nums[0])
            
            else:
                nums[a] = - abs(nums[a])
        
        
        for ans in range(1, n):
            if nums[ans] > 0:
                return ans
        
        if nums[0] > 0:
            return n
        
        return n + 1
             