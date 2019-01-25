class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_code = [".-","-...","-.-.","-..",".",
                      "..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.",
                      "--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alph = ['a','b','c','d','e','f','g','h','i','j',
                'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        morse_dict = dict(zip(alph,morse_code))
        output = []
        for word in words:
            morse = ''
            for char in word:
                morse += morse_dict[char]
            output.append(morse)
        return len(set(output))
                
        
