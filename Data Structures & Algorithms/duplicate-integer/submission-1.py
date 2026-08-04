class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums) == 0: return False
        else: 
            dupes = set()

            for num in nums:
                if num in dupes: return True
                else: dupes.add(num)

        return False



        
        