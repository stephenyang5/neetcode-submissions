class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_value = 0
        l,r = 0, len(heights) - 1

        while l < r:
            curr_value = min(heights[l], heights[r]) * (r-l)

            max_value = max(max_value, curr_value)

            if heights[l]> heights[r]:
                r -=1
            else:
                l+=1
        
        return max_value