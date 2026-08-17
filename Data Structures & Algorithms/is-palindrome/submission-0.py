class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alnum, s_reverse = "", ""
        for char in s:
            char = char.upper()
            if char.isalnum():
                s_alnum += char
                s_reverse = char + s_reverse
        
        return s_alnum == s_reverse