class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product, zero_count = 1,0
        length = len(nums)
         
        for num in nums:
            if num !=0:
                total_product *= num
            else:
                zero_count +=1

        result = [0]* length

        for i in range(length):
            if zero_count == 0:
                result[i] = total_product//nums[i]
            elif zero_count == 1:
                if nums[i] == 0:
                    result[i] = total_product
                    return result
            else:
                return result
        return result