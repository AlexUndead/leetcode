class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True

        def is_symbols(s: str) -> str:
            return not s.upper() == s.lower() or s in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

        clear_s = "".join(filter(is_symbols, s)).lower()

        return clear_s == clear_s[::-1]

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
print(sol.isPalindrome("race a car"))
print(sol.isPalindrome(" "))
print(sol.isPalindrome("0P"))
