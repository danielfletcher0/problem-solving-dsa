class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        grouping = [[] for i in range(len(nums) + 1)]
        counter = {}
        mapp = 0

        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
        

        for key, val in counter.items():
            grouping[val].append(key)
        ans = []
        print(len(grouping))
        for i in range(len(grouping) - 1, -1 , -1):
            for j in grouping[i]:
                if mapp < k:
                    ans.append(j)
                    mapp += 1
        return ans