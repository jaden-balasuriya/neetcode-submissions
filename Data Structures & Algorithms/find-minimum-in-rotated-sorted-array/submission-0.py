class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) -1

        #find the inflection point

        if nums[left] < nums[right]:
            return nums[left]

        while left < right:

            half = ((right+left) // 2)

            if nums[half] > nums[right]:
                left = half +1
            else:
                right = half
        
        return nums[left]
            

            