class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            count = seen.get(num,0) + 1
            seen[num] = count

        heap = []
        for num in seen.keys():
            heapq.heappush(heap, (seen[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result

