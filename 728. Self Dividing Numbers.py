class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        Numbers = []
        for i in range(left, right+1):
            if '0' not in str(i):
                count = 0
                for num in str(i):
                    if i%int(num) == 0:
                        count += 1
                if count == len(str(i)):
                    Numbers.append(i)
        return Numbers
                    
                
            
        
