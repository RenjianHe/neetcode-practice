class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)-1):
            com = target-numbers[i]
            l,r = i+1, len(numbers)-1 
            while l<=r:
                mid = l+(r-l)//2
                if numbers[mid] == com:
                    return [i+1,mid+1]
                elif com<numbers[mid]:
                    r = mid-1
                else:
                    l = mid+1 
        return[]
#using binary search
#O(nlogn), O(n)
                
            
        