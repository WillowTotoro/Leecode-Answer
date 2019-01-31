# Method 1:
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        U = [0,1]
        D = [0,-1]
        L = [-1,0]
        R = [1,0]
        output = [0,0]
        for i in moves:
            if i == 'U':
                output = [x+y for x,y in zip(output,U)]
            if i == 'D':
                output = [x+y for x,y in zip(output,D)]
            if i == 'L':
                output = [x+y for x,y in zip(output,L)]
            if i == 'R':
                output = [x+y for x,y in zip(output,R)]
        if output == [0,0]:
            return True
        else:
            return False
# Method 2:
        U = moves.count('U')
        D = moves.count('D')
        L = moves.count('L')
        R = moves.count('R')
        if U==D and L==R:
            return True
        else:
            return False

                
                
        
