class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num,0) + 1
        count_list = [[] for i in range(len(nums)+1)]
        for num, count in hashmap.items():
            count_list[count].append(num)
        result = []
        for count in range(len(count_list)-1,-1,-1):
            for num in count_list[count]:
                result.append(num)
                if len(result) == k:
                    return result 
