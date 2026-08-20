class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)
        res = heapq.nlargest(k,count.keys(),key=count.get)
        return res
    
    # Hash map with value-frequency pairs + bounded min-heap with heapq module
    # O(n logk), O(n)