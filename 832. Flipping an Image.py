class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        flip = []
        invert = []
        for line in A:
            flipline = line[::-1]
            temp = []
            for i in flipline:
                if i == 0:
                    temp.append(1)
                elif i == 1:
                    temp.append(0)
            invert.append(temp)
        return invert
            
                    
                    
                
        
