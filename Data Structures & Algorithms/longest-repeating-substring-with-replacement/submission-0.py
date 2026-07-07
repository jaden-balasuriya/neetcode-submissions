class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        import string
        def get_replacement():
            return sum(freq.values()) - max(freq.values())


        freq = {}
        uppercase_list = list(string.ascii_uppercase)
        for i in uppercase_list:
            freq[i] = 0

        left = 0
        max_len = 0
        
        freq[s[left]] += 1

        for right in range(1,len(s)):
            freq[s[right]] += 1


            while get_replacement() > k:
                freq[s[left]] -= 1
                left +=1
            
            max_len = max(max_len, right-left +1)
        
        return max_len

        