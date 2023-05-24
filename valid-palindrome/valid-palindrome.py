class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        isValid = True

        if s == "" or s == " ":
            return True


        dummy = ""

        for c in s:
            if not c.isalnum():
                continue
            dummy += c.lower()
        
        left, right = 0, len(dummy) - 1
        while left < right:
            if dummy[left] != dummy[right]:
                isValid = False
            left += 1
            right -= 1
        
        return isValid

