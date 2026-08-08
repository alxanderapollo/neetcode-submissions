
'''
    Solving:
            start with two ptrs starting at the begining and ending sections of the string. 
            if i come across a mismatch do a left traversal after forgiving on the mimatch on the left, if its fine return true
            otherwise do a right traversal after forgiving a mismatch on the right, if its fine return true 
            otherwise return false
        
        if were out of the loop that means there were no deletions that took place and it was a palindrome 
'''


class Solution:
    def traverseOtherSide(self, s:str, i, j)->bool:
        while i < j:
            if s[i].lower() != s[j].lower(): 
                return False
            else:
                i+=1
                j-=1
        return True

    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 0: return True
        i,j = 0, len(s) - 1
        while i < j:
            if s[i].lower() != s[j].lower():
                return self.traverseOtherSide(s, i+1, j) or self.traverseOtherSide(s, i, j-1)
            elif s[i].lower() == s[j].lower(): 
                i+=1
                j-=1
            else: return False
        return True
        
        