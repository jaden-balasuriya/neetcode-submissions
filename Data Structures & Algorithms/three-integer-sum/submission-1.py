class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = set()
        for i in range(len(nums)):
            target_sum = nums[i]
            left = 0
            right = len(nums) -1
            while right > left:
                if right == i:
                    right -=1
                    continue
                if left == i:
                    left +=1
                    continue
                total_sum = target_sum+nums[right]+nums[left]
                if total_sum == 0:
                    tup = tuple(sorted([target_sum,nums[right],nums[left]]))
                    out.add(tup)

                if total_sum >0:
                    right-=1
                else:
                    left+=1
        mylist = [list(i) for i in out]
        return mylist
