class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            if (num-1) not in numSet:
                length = 1
                while (num+length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

# check each number to see if they have a left neighbor, if not, start counting its longest streak. only one traversal, no extra space needed to store results 
# O(n), O(n)