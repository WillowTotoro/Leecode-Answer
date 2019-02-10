class Solution:
    def sortArrayByParityII(self, A: 'List[int]') -> 'List[int]':
        odd_list = []
        even_list = []
        for num in A:
            if num%2:
                odd_list.append(num)
            else:
                even_list.append(num)
        output = []
        for i in range(len(A)):
            if i%2:
                temp = odd_list.pop()
            else:
                temp = even_list.pop()
            output.append(temp)
        return output
