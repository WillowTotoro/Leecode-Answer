class Solution:
    def toLowerCase(self, str):
        res =""
        for char in str:
            if ord(char) in range(65,91):
                res +=chr(ord(char)+32)
            else:
                res+=char
        
        return res
