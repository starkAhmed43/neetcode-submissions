class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([i.lower() for i in s if i.isalnum()])
        # print("Foward = ", s)
        # print("Backward = ", s[-1:(-1*len(s))-1:-1])
        return s == s[-1:-1*len(s)-1:-1]