class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        palindrome = x[::-1]
        if x == palindrome:
            return True
        else:
            return False