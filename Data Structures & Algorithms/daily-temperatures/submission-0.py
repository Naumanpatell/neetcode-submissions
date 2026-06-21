class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n = len(t)
        ans = [0]*n

        for i in range(n):
            for j in range(i+1,n):
                if t[j] > t[i]:
                    ans[i] = j - i
                    break
        return ans 

            
            

