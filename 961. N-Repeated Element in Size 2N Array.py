class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)/2
        A = sorted(A)
        for i in range(len(A)):
            count = 1
            flag = True
            while count < N and flag == True:
                if A[i] == A[i+count]:
                    flag = True
                else:
                    flag = False
                    break
                count += 1

            if flag == True:
                return A[i]
            
    
        
