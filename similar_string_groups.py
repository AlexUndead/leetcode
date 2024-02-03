import pdb
from typing import List

# https://leetcode.com/problems/similar-string-groups/
# Первый заход. Не проходит тест: 
#assert sol.numSimilarGroups(["kccomwcgcs","socgcmcwkc","sgckwcmcoc","coswcmcgkc","cowkccmsgc","cosgmccwkc","sgmkwcccoc","coswmccgkc","kowcccmsgc","kgcomwcccs"]) == 5
# Проблема в том что похожие сторки могут приходить не в том порядке (связующая строка С которая связывает непохожие строки между собой А и В приходит последний)
#class Solution:
#    def is_similar(self, string, similar_string):
#        """'tars' -> 'rats'"""
#        no_similar_count = 0
#        no_similar_index = []
#        for number, symbol in enumerate(string):
#            if symbol != similar_string[number]: 
#                no_similar_count += 1
#                no_similar_index.append(number)
#            if no_similar_count > 2:
#                return False
#
#        if no_similar_count:
#            if len(no_similar_index) != 2:
#                return False
#            else:
#                if string[no_similar_index[0]] != similar_string[no_similar_index[1]]:
#                    return False
#                if string[no_similar_index[1]] != similar_string[no_similar_index[0]]:
#                    return False
#
#        return True
#
#    def numSimilarGroups(self, strs: List[str]) -> int:
#        similar_groups = []
#
#        for string in strs:
#            str_add = False
#            for group in similar_groups:
#                for similar_string in group:
#                    if self.is_similar(string, similar_string):
#                        group.append(string)
#                        str_add = True
#                        break
#                if str_add:
#                    break
#
#            if not str_add:
#                similar_groups.append([string])
#
#        return len(similar_groups)

#Правильное решение (пришлось читать ответ задачи, сам бы на 01.05.2023 не догадался)
# Ты молодец, все завелось почти сразу
class Solution:
    def is_similar(self, string, similar_string):
        """'tars' -> 'rats'"""
        no_similar_count = 0
        no_similar_index = []
        for number, symbol in enumerate(string):
            if symbol != similar_string[number]: 
                no_similar_count += 1
                no_similar_index.append(number)
            if no_similar_count > 2:
                return False

        if no_similar_count:
            if len(no_similar_index) != 2:
                return False
            else:
                if string[no_similar_index[0]] != similar_string[no_similar_index[1]]:
                    return False
                if string[no_similar_index[1]] != similar_string[no_similar_index[0]]:
                    return False

        return True

    def count_top(self, name, cache, glav=False):
        if name in cache:
            return

        top = self.edges[name]
        if glav and not top["visited"]:
            self._count_graphs += 1
        cache[name] = True
        top["visited"] = True

        for link in top["links"]:
            self.count_top(link, cache=cache)


    def count_graphs(self):
        self._count_graphs = 0

        for edge in self.edges:
            cache = {}
            self.count_top(edge, glav=True, cache=cache)

    def numSimilarGroups(self, strs: List[str]) -> int:
        self.edges = {i:{"links": [], "visited": False} for i in strs}
        for number, _str in enumerate(strs):
            for srav_str in strs[number + 1:]:
                if self.is_similar(_str, srav_str):
                    self.edges[_str]["links"].append(srav_str)
                    self.edges[srav_str]["links"].append(_str)

        self.count_graphs()
        return self._count_graphs

sol = Solution()
#assert sol.is_similar("tars", "rats") == True
#assert sol.is_similar("rats", "arts") == True
#assert sol.is_similar("arts", "star") == False
assert sol.numSimilarGroups(["tars","rats","arts","star"]) == 2
assert sol.numSimilarGroups(["omv","ovm"]) == 1
assert sol.numSimilarGroups(["abc","abc"]) == 1
assert sol.numSimilarGroups(["aba","abc"]) == 2
#assert sol.numSimilarGroups(["cowkccmsgc","kowcccmsgc"]) == 1
assert sol.numSimilarGroups(["coswmccgkc","cosgmccwkc"]) == 1
assert sol.numSimilarGroups(["coswcmcgkc","cosgmccwkc"]) == 2
assert sol.numSimilarGroups(["coswcmcgkc","cosgmccwkc", "coswmccgkc"]) == 1
assert sol.numSimilarGroups(["kccomwcgcs","socgcmcwkc","sgckwcmcoc","coswcmcgkc","cowkccmsgc","cosgmccwkc","sgmkwcccoc","coswmccgkc","kowcccmsgc","kgcomwcccs"]) == 5
