#https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            result = ""
            rev = list(str(x))
            rev.reverse()
            for i in rev:
                result += i

            return int(result) == x
