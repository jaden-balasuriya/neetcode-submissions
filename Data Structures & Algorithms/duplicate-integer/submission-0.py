class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        pyset = set()
        for i in nums:
            pyset.add(i)
        return len(nums) != len(pyset)