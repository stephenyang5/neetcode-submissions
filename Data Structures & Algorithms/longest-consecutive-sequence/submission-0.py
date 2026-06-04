class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        seen = set(nums)

        for num in nums:
            curr_length, curr = 0, num
            while curr in seen:
                curr_length +=1
                curr +=1
            max_length = max(curr_length, max_length)

        return max_length