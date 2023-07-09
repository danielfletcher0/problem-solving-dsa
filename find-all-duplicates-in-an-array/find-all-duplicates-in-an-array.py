class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counter = collections.defaultdict(bool)
        ans = []

        for num in nums:
            if counter[num]:
                ans.append(num)
            counter[num] = True
        return ans