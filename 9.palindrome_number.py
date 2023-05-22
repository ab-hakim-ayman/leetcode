class Solution:
    def isPalindrome(self, x: int):
        s: str = str(x)
        left, right = 0, len(s)-1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -=1
        return True
    
s = Solution()
result = s.isPalindrome(121)
print(result)