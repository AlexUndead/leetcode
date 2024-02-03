from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = defaultdict(lambda: 0)

        for i in s:
            counter[i] += 1

        _sum = 0
        has_nechet = False

        for sym in counter:
            if counter[sym] % 2 != 0:
                _sum += counter[sym] - 1
                has_nechet = True
            else:
                _sum += counter[sym]

        if has_nechet:
            _sum += 1
        return _sum



sol = Solution()
print(sol.longestPalindrome("abccccdd"))
print(sol.longestPalindrome("abCcccdd"))
print(sol.longestPalindrome("ccc"))
print(sol.longestPalindrome("a"))
print(sol.longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"))




        
