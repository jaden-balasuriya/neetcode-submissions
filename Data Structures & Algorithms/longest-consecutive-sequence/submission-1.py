class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #edge case:
        if len(nums) == 0:
            return 0


        # list of (start,end), add or subtract to it
        myset = set()

        for i in nums:
            myset.add(i)

        largest = 1
        
        for i in nums:
            if i-1 in myset:
                continue
            j = 1
            while i+j in myset:
                j+=1
            if j > largest:
                largest = j
        return largest
                

