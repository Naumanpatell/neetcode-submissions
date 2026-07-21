class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j = 0, len(heights) - 1
        mostwater = 0
        while i<j:
            height = min(heights[i],heights[j])#
            base = j-i
            value = height*base
            mostwater = max(value, mostwater)

            if heights[i] <= heights[j]:
                i+=1
            else:
                j-=1
        return mostwater