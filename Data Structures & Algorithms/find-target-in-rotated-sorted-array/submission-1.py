class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binsearch(left,right):
            while left <= right:
                half = (left+right)//2
                if nums[half] == target:
                    return half
                elif nums[half] < target:
                    left = half + 1
                else:
                    right = half -1
            return -1
        left = 0

        right = len(nums)-1

        #get min
        while left < right:
            half = (left+right)//2

            if nums[half] > nums[right]:
                left = half + 1
            else:
                right = half
        

        return max(binsearch(left,len(nums)-1),binsearch(0,left))