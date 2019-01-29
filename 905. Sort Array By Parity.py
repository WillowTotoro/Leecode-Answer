class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        oddlist = []
        evenlist = []
        for num in A:
            if num % 2:
                oddlist.append(num)
            else:
                evenlist.append(num)
        return evenlist+oddlist
