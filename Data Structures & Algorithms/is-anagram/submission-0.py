class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        master_dict = {}
        for i in range(len(s)):
            if s[i] in master_dict:
                master_dict[s[i]] += 1
            else:
                master_dict[s[i]] = 1
            if t[i] in master_dict:
                master_dict[t[i]] -= 1
            else:
                master_dict[t[i]] = -1


        return not any(master_dict.values())