class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        rain = 0

        for i in range(len(height)):
            l = r = height[i]
            for j in range(i):
                l = max(l, height[j])
            for k in range(i + 1, len(height)):
                r = max(r, height[k])

            rain += min(l,r) - height[i]
        
        return rain
                