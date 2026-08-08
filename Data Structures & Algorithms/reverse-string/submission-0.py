'''

    0. return a reversed string, do the reversing in place
    1.
    ''->''
    'a'->'a'
    'ab' -> 'ba'

    'abc'->'cba'

    2.
        if the array is empty or has a single element return those arrays 
        using two pointers starting from the begning and ending indices, swap the elements at those indices continue until the indices converge in the middle
    
    3. 
    if the array is empty or has a single element: return

    - create two ptrs starting at the begining and end of the array
    while the two ptrs havent crossed walk them towards one another
        swap the elements of two ptrs and walk towards eacher other 

    return the reversed string



'''



class Solution:
    def reverseString(self, s: List[str]) -> None:
        if len(s) <= 0: return s
        i,j = 0, len(s) - 1
        while i < j:
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1

        