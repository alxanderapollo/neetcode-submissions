'''
    0.return an element whose frequency is > arrayLen/2
    1.
       A. [1,1,1,1] - > arrayLen = 4/2 = 2
        1: 4
        4>2
        return 1

       B.[]-> None
       C. [1,1,2,2]
            arrayLen = 4/2 = 2
            1:2
            2:2
    2.
        [5,5,1,1,1,5,5]
        1. Iterate through the array O(n) linear time
        2. store each number by its frequency O(n) storing
        3. pull the number with the highest freuqncy and return that 
    3.
        if len(arr) == 0 : return nothing
        elif len(arr) == 1: return that first number in the array
        else:
            -create a map
            iterate through array elt:
                store each number: if its the first time seeing it set frequency to 1 otherwise append +=1
            
            pull out the key with the largest frequency and then pull out the key and return that as an asnwer 




'''


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 0 : return None
        elif len(nums) == 1: return  nums[0]
        else:
            frequency = Counter(nums)  
          # most_common(1) returns a list containing a tuple: [(number, frequency)]
            
                    
            return frequency.most_common(1)[0][0]
        