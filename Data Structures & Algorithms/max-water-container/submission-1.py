class Solution:
    def maxArea(self, height: List[int]) -> int:
        i ,j = 0 ,len(height) - 1
        max_value = 0
        while i < j:
            length = min(height[i],height[j])
            distance = j-i
            value = length*distance
            max_value = max(max_value, value)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
            
        return max_value
