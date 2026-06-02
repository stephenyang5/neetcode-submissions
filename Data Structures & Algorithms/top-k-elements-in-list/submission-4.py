class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            count = seen.get(num,0) + 1
            seen[num] = count

        test_list = []
        for key,value in seen.items():
            test_list.append((key,value))
        
        test_list.sort(key=lambda x:x[1],  reverse=True)

        return_list = []
        for i in range(k):
            return_list.append(test_list[i][0])
        return  return_list
