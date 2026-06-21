class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n =  len(t)
        ans = [0]*n
        stack = []

        for i in range(n):
            while stack and t[i] > t[stack[-1]]:
                p_idx = stack.pop()
                ans[p_idx] = i - p_idx
            stack.append(i)
        return ans
            
            

