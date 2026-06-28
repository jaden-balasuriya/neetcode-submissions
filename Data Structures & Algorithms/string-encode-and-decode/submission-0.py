class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for i in strs:
            output+= str(len(i))
            output+= "#"
            output+= i
        return output
    def decode(self, s: str) -> List[str]:
        outlist = []
        modeNum=True
        numstr=""
        number = 0
        outstr = ""
        
        i = 0

        while i < len(s):
            numstr=""
            while s[i] != "#":
                numstr+=s[i]
                i+=1
            i+=1
            number = int(numstr)
            j = 0
            while j < number:
                outstr += s[i+j]
                j+=1
            outlist.append(outstr)
            i+=j
            outstr=""
                

        return outlist