from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for anagram in strs:
            groups[tuple(sorted(anagram))].append(anagram)

        return [group for group in groups.values()]
        

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(sol.groupAnagrams(["a"]))
print(sol.groupAnagrams([""]))
