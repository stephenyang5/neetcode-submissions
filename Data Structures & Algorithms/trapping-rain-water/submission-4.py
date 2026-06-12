class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l,r = 0, len(height) - 1
        l_max, r_max = height[0], height[r]
        rain = 0

        while l < r:
            if l_max < r_max:
                l +=1
                l_max = max(l_max, height[l])
                rain += l_max - height[l]
            else:
                r -=1
                r_max = max(r_max, height[r])
                rain += r_max - height[r]
        return rain