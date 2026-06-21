class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = [0]*26
        maxfreq = 0
        result = 0
        for right in range(len(s)):
            count[ord(s[right]) - ord('A')] += 1
            maxfreq = max(maxfreq, count[ord(s[right]) - ord('A')])

            while (right-left+1) - maxfreq > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            result = max(result, right-left+1)
        return result 

            


            
