class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
     
        if not nums or len(nums) == 1 and nums[0] == val: return 0 
        i, j = 0, len(nums) - 1
        # first pass O(n) swap out the values we dont want
        while i < j:
            while(nums[j] == val and j >= 0):j-=1

            if i > j: break
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -=1
            else: 
                i +=1
        
        return j +1


        