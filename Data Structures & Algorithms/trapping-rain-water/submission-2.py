class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        stack = []
        rain = 0

        for i in range(len(height)):
            while stack and height[i]>=height[stack[-1]]:
                mid = height[stack.pop()]
                if stack:
                    r = height[i]
                    l = height[stack[-1]]
                    h = min(r,l) - mid
                    w = i - stack[-1] -1
                    rain += h * w

            stack.append(i)

        return rain
                