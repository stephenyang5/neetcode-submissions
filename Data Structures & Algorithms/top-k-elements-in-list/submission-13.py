class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            count = seen.get(num,0) + 1
            seen[num] = count

        buckets = [[] for i in range(len(nums)+1)] 

        for key,value in seen.items():
            buckets[value].append(key)
        
        results = []
        for i in range(len(buckets)-1, 0, - 1):
            for num in buckets[i]:
                results.append(num)
                if len(results) ==k:
                    return results


        