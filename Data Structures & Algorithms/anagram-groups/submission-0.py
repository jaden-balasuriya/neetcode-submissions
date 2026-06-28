class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}
        for i in strs:
            sort_str = "".join(sorted(i))
            if sort_str not in mydict:
                mydict[sort_str] = []
            mydict[sort_str].append(i)
        output = []
        for i in mydict.values():
            output.append(i)
        return output
        