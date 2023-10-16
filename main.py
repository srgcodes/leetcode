#this is finding longest common prefix from the given list of words #leetcode.
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""             #which will be our base condition if the string is empty or there is nothing common.
        new_strs=sorted(strs)
        first_word=new_strs[0]
        for i in range(len(first_word)):
            if first_word[i]!=new_strs[-1][i]:
                return first_word[:1]
        return first_word


