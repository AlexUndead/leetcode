class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(left, right) -> bool:
            while left < right: 
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        for length in range(len(s), 0, -1):
            start = 0

            while True:
                if is_palindrome(start, length - 1):
                    return s[start: length]

                if len(s) == length:
                    break
                else:
                    start += 1
                    length += 1

sol = Solution()
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("cbbd"))

