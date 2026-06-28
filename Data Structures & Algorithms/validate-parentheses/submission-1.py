class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s)%2 !=0:
            return False
        for i in s:
            if i in ["[","{","("]:
                stack.append(i)
            else:
                if not stack:
                    return False
                item = stack.pop()
                if i == "]" and item !="[":
                    return False
                if i == "}" and item !="{":
                    return False
                if i == ")" and item !="(":
                    return False
        if not stack:
            return True
        return False

            
