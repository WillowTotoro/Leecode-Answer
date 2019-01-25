import collections
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        d = collections.defaultdict(int)
        for s in S:
            d[s] += 1
        for j in J:
            if j in J:
                count += d[j]                
        return count
        
