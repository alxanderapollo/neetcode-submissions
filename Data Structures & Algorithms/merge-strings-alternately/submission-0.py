
'''
    0. return a string that contains a combo of both inputs
    1. 
        a= '', b = ''
        c = ''

        a=o, b = ''
        c = o

        normal calse
        Input: word1 = "abc", word2 = "xyz"
        Output: "axbycz"

        Corner case 
        Input: word1 = "ab", word2 = "abbxxc"
        Output: "aabbbxxc"
    
    2. 
        -create two ptrs
        - create a returning resulting string

        iterate through both arrays using those ptrs:
            alternate adding to the string
        
        if the indices dont ewual length of the arrays thats when we take the corresponding ptrs and splice out 
        from x..n exclusive and append that range into the resulting string 



'''


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        if len(word1) == 0 and len(word2) == 0: return word1
        elif len(word1) >= 0 and len(word2) == 0: return  word1
        elif  len(word2) >= 0 and len(word1) == 0: return  word2
        else:
            i,j = 0,0
            result = ''

            while i < len(word1) and j < len(word2):
                result+= word1[i] + word2[j]
                i+=1
                j+=1

            print('whats left of i ', i)
            print('whats left of j ', j)

            if i < len(word1): result+= word1[i:]
            if j < len(word2): result+= word2[j:]

            return result





        