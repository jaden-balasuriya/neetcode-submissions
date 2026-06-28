class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0
        zero_index = 0
        for i in range(len(nums)):
            if nums[i] !=0:
                prod *=nums[i]
            else:
                zero_count+=1
                zero_index = i
        if zero_count >= 2:
            return [0]*len(nums)
        elif zero_count == 1:
            output = [0]*len(nums)
            output[zero_index] = prod
            return output
        else:
            return [prod//nums[i] for i in range(len(nums))]