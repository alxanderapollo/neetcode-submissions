class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        store = {}
       
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in store: return [store[compliment], i]
            
            store[num] = i
        return []
        