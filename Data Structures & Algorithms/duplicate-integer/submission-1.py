class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        nums.sort()
        temp = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == temp:
                return True
            else:
                temp = nums[i]
        return False