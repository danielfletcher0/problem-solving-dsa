class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        matching = defaultdict(list) #for mapping  charCount to list of anangrams

        for i in strs:
            count = [0] * 26 #represents the alphabet a - z

            for c in i:
                count[ord(c) - ord("a")] += 1 #Updates the count of the specific letter in the count array
            
            matching[tuple(count)].append(i)
        
        return matching.values()
        