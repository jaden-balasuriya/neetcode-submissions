class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        
        for i in range(len(nums)):
            diff = target-nums[i]
            if nums[i] in mydict:
                j = mydict[nums[i]]
                if i < j:
                    return [i,j]
                else:
                    return [j,i]
            mydict[diff] = i
        return []