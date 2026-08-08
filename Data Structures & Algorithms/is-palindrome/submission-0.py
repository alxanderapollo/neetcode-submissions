class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 0: return True
        i,j = 0, len(s) - 1
        while i < j:

            # make it ignore characters that arent alphanumeric
            if  not s[j].isalnum(): 
                j-=1
                continue

            if not s[i].isalnum(): 
                i+=1
                continue
            # must be case sensetive 
            elif s[i].lower() == s[j].lower(): 
                i+=1
                j-=1
            else: return False
        
        return True

        