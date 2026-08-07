class Solution:

    def encode(self, strs: List[str]) -> str:
        string_encoded = ''
        for string in strs:
            string_encoded += str(len(string)) +':'+string
        return string_encoded

    def decode(self, s: str) -> List[str]:
        list_of_strings = []
        # three things to extract
        # 5:Hello5:World

        '''
            if j == :
                take everything before : and that will be the number store that
                then iterate by the number of times that will be our word store that into an array
                repeat until were done 
        '''
        ans = []
        i = 0 
        j = i+1
        length_of_currStr = 0
        while i < len(s):
            if s[j] ==':':
                # extract number from i - j
                length_of_currStr = int(s[i:j])
                # pullout the string
                k = j + 1
                currentStr = ''
                while length_of_currStr > 0:
                    currentStr += s[k]
                    k+=1
                    length_of_currStr -=1
                ans.append(currentStr)
                i = k
                j = i +1
            else: 
                j +=1




        
        return ans
