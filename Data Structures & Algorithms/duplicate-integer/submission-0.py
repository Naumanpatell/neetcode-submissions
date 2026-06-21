class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_list = []
        flag = True
        for num in nums:
            if num in hash_list:
                return True
                break
            else:
                hash_list.append(num)
        if nums == hash_list:
            return False 