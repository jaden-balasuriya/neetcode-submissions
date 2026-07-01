class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) ==0:
            return 0
        if len(s) == 1:
            return 1
        
        maxLen = 1
        left = 0
        right = 0

        letter = set()


        while right < len(s) -1:
            right += 1

            if s[right] in letter:
                while s[left] != s[right]:
                    letter.remove(s[left])
                    left+=1
                left+=1
            letter.add(s[left])
            letter.add(s[right])

            maxLen = max(maxLen,len(letter))
                

        return maxLen
        
