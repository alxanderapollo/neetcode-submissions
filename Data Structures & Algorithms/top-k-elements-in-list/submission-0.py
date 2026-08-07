'''
1. return an array that represents the top frquent numbers in the given array. Where k = the number of frequent numbers expected to be returned
2. 
    [1,2,2,3,3,3]
    1: 1
    2:2
    3:3
    k = 2
    [3,2]

    [1], k = 2
    ->[1]

    k=0
    [1,2,3,4]
    ->[]

3. 
    using counter to store each num into the map
    frequency = Counter(array)
    ans- array store the top k elements

    Find the top freq and then delete it
        decrement k 
        repeat until k == 0

    return array

4.
    if len(array) <= 1: return the current array
    else:
        create a map to store all the numbers using the counter library
        iterate through the map and find the largest value, after that delete that key value pairing after storing it in the return array 
        repeat until done
    return array 
'''

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(nums) <= 1: return nums
        else:
            frequency = Counter(nums)
            ans = []
           
            while k > 0:
                largest_num = float('-inf')
                chosen_key = -99
                for key, val in frequency.items():
                    if val > largest_num:
                        chosen_key = key
                        largest_num = val   
                
                ans.append(chosen_key)
                del frequency[chosen_key]
                k -=1
            return ans 
                



           



        