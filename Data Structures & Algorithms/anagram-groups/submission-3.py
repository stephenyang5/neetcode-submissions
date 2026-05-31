class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        total_list = {}

        for string in strs:
            count = [0]*26
            for char in string:
                index = ord(char) - ord('a')
                count[index] +=1
            
            key = tuple(count)
            if key not in total_list:
                total_list[key] = [string]
            else:
                total_list[key].append(string)
        
        return [total_list[key] for key in total_list]

