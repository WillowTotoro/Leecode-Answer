class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        absA = [abs(i) for i in A]
        sortA = sorted(absA)
        squareA = [i*i for i in sortA]
        return squareA
