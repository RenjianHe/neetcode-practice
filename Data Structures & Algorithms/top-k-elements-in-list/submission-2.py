class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)
        frq = []
        for num, cnt in count.items():
            frq.append([cnt,num])
        frq.sort()
        res = []
        while len(res)<k:
            res.append(frq.pop()[1])
        return res
    
    # hash map with value-frequency pairs + sorting based on frequencies
    # O(n log n), O(n) 
        