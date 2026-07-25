class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow2 = nums[0]
        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]
        return slow

# Revised: 11 july 2026 --> written without any mistakes
# Revised 25 july 2026 --> wrote the linkedlist version by mistake but was able convert it to array version(Mistake --> While loop condition wrong )