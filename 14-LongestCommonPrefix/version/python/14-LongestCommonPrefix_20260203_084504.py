# Last updated: 2/3/2026, 8:45:04 AM
1class Solution(object):
2    def longestCommonPrefix(self, strs):
3        """
4        :type strs: List[str]
5        :rtype: str
6        """
7        str0 = strs[0]
8        
9        for idx1 in range(len(str0)):
10            char = str0[idx1]
11            for idx2 in range(1,len(strs)):
12                if idx1 ==len(strs[idx2]) or strs[idx2][idx1] != char:
13                    return str0[:idx1]
14        return str0
15        
16