class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        left = 0
        right = len(heights) -1
        def getArea(i,j):
            width = abs(i-j)
            height = min(heights[i],heights[j])
            area = width*height
            return area
        #brute force

        while right > left:
            if getArea(left,right) > maxWater:
                maxWater = getArea(left,right)
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
            
            
        return maxWater