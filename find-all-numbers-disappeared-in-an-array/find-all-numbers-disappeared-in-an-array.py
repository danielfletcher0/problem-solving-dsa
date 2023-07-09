class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        mapp = set(nums)


        for i in range(1, len(nums) + 1):
            if i not in mapp:
                ans.append(i)
        
        return ans