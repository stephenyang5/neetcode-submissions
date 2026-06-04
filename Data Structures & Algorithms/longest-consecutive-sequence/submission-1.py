class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sorted_nums = sorted(nums)
        max_length = 0
        curr = sorted_nums[0]
        curr_length = 1
        i = 0
        for i in range(1, len(nums)):
            if sorted_nums[i-1] == sorted_nums[i]:
                continue
            
            if sorted_nums[i] - sorted_nums[i-1] == 1:
                curr_length +=1
            else:
                max_length = max(max_length, curr_length)
                curr_length = 1

        return max(max_length, curr_length)
