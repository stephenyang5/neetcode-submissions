class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i, num in enumerate(nums):

            if i > 0 and num == nums[i - 1]:
                continue

            l,r = i+1, len(nums)-1
            while l<r:
                curr = num + nums[l] + nums[r]

                if curr > 0:
                    r -= 1
                elif curr < 0:
                    l +=1
                else:
                    output.append([num, nums[l], nums[r]])
                    r-=1
                    l+=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
        return output
        


