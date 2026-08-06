
'''
0. modify the  array in place -> sort the numbers in ascenind order
1. 
    Normal Cases
        [1,0,1,2] -> [0,1,1,2]
        [1] -> [1]
    
    Edge cases
            [] -> []
            None -> []
2.Approach
    1st pass count each of the colors by storing them in map O(n) store and read
    2nd read out the key values pairs replacing the array with the colors as they appeared

3.
    if the array is empty or a single element: return
    else:
            -create a map
            -Create a val to hold the largest number
            for every number in the array:
                create the key/val pairing
            
            for every key/val pairing: 
                pull out the smallest number and add the the array - # of times it appeared

'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if not nums or len(nums) == 1: return
        else:
            store_nums = {}
            for  number in nums:
                if number not in store_nums: store_nums[number] = 1
                else: store_nums[number] +=1
        


        index = 0
        color = 0
        while color <= 2:
            # grab the frequency
            frequency = store_nums.get(color, 0)
            count = 0
            # while the count is less than the frequency
            # go to the indexed postion and write the color
            while count < frequency:
                nums[index] = color
                index += 1
                count += 1
            color += 1

        