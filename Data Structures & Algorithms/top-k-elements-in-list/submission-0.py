class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create freq chart
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 0
            freq[i]+= 1
        sorted_arr =  sorted(freq.items(),key=lambda item: item[1],reverse=True)
        return [item[0] for item in sorted_arr[0:k]]